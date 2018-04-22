# SAS-Batch-Submit-Server
Web Interface SAS Batch Submit Server<BR>
The is a web based server system written mainly in perl script where you can batch run your SAS code, monitor the job status and 
view the SAS log and results through a web browser like Firefox or Chrome.

## Prerequisites
Linux OS, and Ubuntu 16.04 LTS or higher are preferred;<br>
SAS: SAS 9.4 or higher are preferred;<br>
Python 3 (Included in most Linux based distribution);<br>
Perl 5 (Included in most Linux based distribution);<br>

## Pre-setting
git clone git://github.com/fanfanpao/SAS-Batch-Submit-Server.git<br>

The default path is /home/user/Downloads/git/SAS-Batch-Submit-Server.<br>
If not, you need to change the path setting for the following files:<br>
./scriptsmax.sh<br>
./fanfanpao/base.txt<br>
./fanfanpao/cgi-bin/fanfanpao.pl<br>

Make sure you have soft link with SAS:<br>
sudo link /usr/local/SASHome/SASFoundation/9.4/bin/sas_en /usr/local/bin/sas941<br>

## Start the Server
Under SAS-Batch-Submit-Server folder, open the terminal:<br>
Input "./scriptmax.sh", then enter.<br>
Leave Terminal window open and the server will run on the background.<br>

Open your web browser, such as Firefox (57.0 or higher are preferred) or Chrome, then enter<BR>
http://localhost:8000/cgi-bin/main2.cgi<br>

## Login the Server
You can use the default user name "sastest" and password "123456" to log in.
Or you can register one new account if needed.



