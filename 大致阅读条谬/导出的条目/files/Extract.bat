@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo 正在提取当前目录下所有子文件夹中的文件...
echo.

rem 获取当前目录路径
set "current_dir=%cd%"

rem 计数器
set file_count=0
set folder_count=0

rem 遍历所有子文件夹
for /d %%d in (*) do (
    if exist "%%d\" (
        set /a folder_count+=1
        echo 正在处理文件夹: %%d
        
        rem 移动该文件夹内的所有文件到当前目录
        for %%f in ("%%d\*.*") do (
            if exist "%%f" (
                set /a file_count+=1
                echo   移动文件: %%~nxf
                move "%%f" "%current_dir%\"
            )
        )
    )
)

echo.
echo 操作完成！
echo 共处理了 !folder_count! 个文件夹
echo 共移动了 !file_count! 个文件
echo.
echo 注意：
echo 1. 如果存在同名文件，后处理的会覆盖先处理的
echo 2. 子文件夹中的子文件夹不会被处理
echo 3. 子文件夹本身不会被删除
echo.
pause