@rem 启动纹脉的本地静态预览服务。
@echo off
cd /d "%~dp0"
node scripts/serve.mjs
pause
