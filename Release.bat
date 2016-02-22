@echo off
cd ..
cd C:\octpuslogs
call :loghere > %1.txt
cd C:\OctopusTools.2.5.10.39
echo publishing %1
octo deploy-release --project %1 --releaseNumber latest --deployto Production --skip "Confirm deployment to production" --server getServer --apikey getAPIKey
PING 1.1.1.1 -n 1 -w 10000 >NUL
:loghere
cd ..

