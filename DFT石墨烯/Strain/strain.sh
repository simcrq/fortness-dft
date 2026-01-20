#!/bin/bash
BASE_A1_X=2.4600000028969773
BASE_A2_X=-1.2300000014484886
BASE_A2_Y=2.1304224958185749
BASE_Z=20.0000000000000036
START_STRAIN=0.200
END_STRAIN=0.200
STEP_STRAIN=0.001  # 至少三位小数步长，确保 0.205 不被四舍五入

for strain in $(seq -f "%.3f" $START_STRAIN $STEP_STRAIN $END_STRAIN)
do
    DIR_NAME="strain_${strain}"
    
    if [ -d "$DIR_NAME" ]; then
        echo "文件夹 $DIR_NAME 已存在，跳过..."
        continue
    fi
    
    mkdir "$DIR_NAME"
    echo "准备应变: $strain (文件夹: $DIR_NAME)"

    # 精确计算缩放因子（bc 默认整数精度会截断小数，改用 awk 保留精度）
    scale=$(awk "BEGIN {printf \"%.10f\", 1.0 + $strain}")

    new_a1_x=$(awk "BEGIN {printf \"%.10f\", $BASE_A1_X * $scale}")
    new_a2_x=$(awk "BEGIN {printf \"%.10f\", $BASE_A2_X * $scale}")
    new_a2_y=$(awk "BEGIN {printf \"%.10f\", $BASE_A2_Y * $scale}")
    
    new_z=$BASE_Z

    cat > "$DIR_NAME/POSCAR" <<EOF
Graphene_Strain_$strain
1.0
 $new_a1_x  0.0000000000  0.0000000000
 $new_a2_x  $new_a2_y  0.0000000000
 0.0000000000  0.0000000000  $new_z
C
2
Direct
0.3333333333333357  0.6666666666666643  0.0000000000000000
0.6666666666666643  0.3333333333333357  0.0000000000000000
EOF

    cp INCAR.st "$DIR_NAME/"
    cp KPOINTS "$DIR_NAME/"
    cp POTCAR "$DIR_NAME/"
    
    # 提交任务
done

echo "done"
