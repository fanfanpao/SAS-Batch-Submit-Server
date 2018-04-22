cd /home/user/Downloads/git/SAS-Batch-Submit-Server/fanfanpao/
chmod +x ./cgi-bin/*.cgi
chmod +x ./cgi-bin/*.pl
./cgi-bin/fanfanpao.pl &
python3 -m http.server --cgi
