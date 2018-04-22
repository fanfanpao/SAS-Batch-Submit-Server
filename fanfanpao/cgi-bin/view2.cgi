#!/usr/bin/perl
##
##  view2 -- CGI program that display the content of log or output files
##

###########################################################################
# Get Form Information
&parse_form;

# Read Main Page
&main_page;

#######################
# Parse Form Subroutine

sub parse_form {

   $req=$ENV{'REQUEST_METHOD'};

   # Get the input

   if ($ENV{'REQUEST_METHOD'} eq "GET")
   {
        $buffer = $ENV{'QUERY_STRING'};
   }
   else
   {
	read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   }

   # Split the name-value pairs
   @pairs = split(/&/, $buffer);

   foreach $pair (@pairs) {
      ($name, $value) = split(/=/, $pair);

      # Un-Webify plus signs and %-encoding
      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
      $value =~ s/<!--(.|\n)*-->//g;

#      if ($allow_html != 1) {
#         $value =~ s/<([^>]|\n)*>//g;
#     }
#     else {
#        unless ($name eq 'body') {
#         $value =~ s/<([^>]|\n)*>//g;
#         }
#      }
	  
	  if ($name ne "source") {
         $value =~ s/<([^>]|\n)*>//g;	  
	  }
	  
      $FORM{$name} = $value;
   }
}

###############################
# Main Page Subroutine

sub main_page {

   	open(BAS, "base.txt") || &error;
    	while (<BAS>)
    	{
		chop();
		($basedir, $info) = split(/\|/);	
    	}    
    	close(BAS);
		
	open(UPW, "pswd2.cgi") || &error;
    	
	while (<UPW>)
    {
		chop();
		my($usrnamef, $usrpwdf, $usrtypef, $usremailf, $usrpathf) = split(/:/);	
#		$usrpwdf{$usrnamef} = $usrpwdf;
		$usrpwdf{$usrnamef} = crypt($usrpwdf, substr($usrnamef,0,2));			
		$usrtypef{$usrnamef} = $usrtypef;
		$usremailf{$usrnamef} = $usremailf;
		$usrpathf{$usrnamef} = $usrpathf;

    }    
    close(UPW);	
		
	print "Content-type: text/html; charset=iso-8859-1\n\n";

      	$usrid = $ENV{'HTTP_COOKIE'};
      	$usrid =~ /usrid=([^;]*)/;
      	$usrid = $1;
		
      	$usremail = $ENV{'HTTP_COOKIE'};
      	$usremail =~ /usremail=([^;]*)/;
      	$usremail = $1;
		
      	$usrkey = $ENV{'HTTP_COOKIE'};
      	$usrkey =~ /usrkey=([^;]*)/;
      	$usrkey = $1;			
		
   if ($usrid eq "" or $usrpwdf{$usrid} ne $usrkey) 
   {
	print "<meta http-equiv=\"refresh\" content=\"0; URL=main2.cgi\">\n";
	print "<a href=\"main2.cgi\">You must logon from ScriptsMax.com main page</a>\n";
   } 
   else
   {
	print "<html><head><title>ScriptsMax.com (Beta)</title>\n";

	print "<STYLE type=text/css>H2 {FONT-SIZE: 16px; FONT-FAMILY: Verdana, Arial, Helvetica, sans-serif}\n";
	print "TH {FONT-SIZE: 12px; FONT-FAMILY: Verdana, Arial, Helvetica, sans-serif}\n";
	print "TD {FONT-SIZE: 12px; FONT-FAMILY: Verdana, Arial, Helvetica, sans-serif}\n";
	print "LI {FONT-SIZE: 12px; FONT-FAMILY: Verdana, Arial, Helvetica, sans-serif}\n";
	print "TEXTAREA {WIDTH: 100%}\n";		
	print "INPUT {FONT-SIZE: 14px}\n";
	print "</STYLE>\n";
      print "</head>\n";

      print "<body bgColor=#eaf9ff><center>\n";

      print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
      print "  <tr><td bgcolor=white align=center background=\"../image/cloud.jpg\"><br><br>\n";
      print "  <h1>ScriptsMax.com (Beta)</h1>\n";
      print "  <h2>Cloud Computing for SAS, R and other Scripts</h2><br></td></tr>\n";
      print "</table><br>\n";

      print "<Table cellSpacing=0 cellPadding=0 width=100% border=0>\n";
      print "  <tr>\n";
      print "     <td valign=top width=200 bgcolor=#dbe6e0>\n";
      print "       <FORM method=POST ACTION=\"main2.cgi\">\n";
      print "       <TABLE cellSpacing=0 cellPadding=4 width=200 border=0>\n";

      print "           <TR bgColor=#99bcd8><TD colspan=2 align=left><font color=\"white\"><b>USER</b></font></TD></TR>\n";
      print "           <TR><TD colspan=2 align=left><img src=\"../image/user.png\" border=0> User: $usrid</TD></TR>\n";
      print "           <TR><TD colspan=2 align=center><INPUT TYPE=\"submit\" name=\"action\" value=\"Logout\"></TD></TR>\n";
      print "           <tr><td colspan=2 height=8 bgcolor=EAF9FF></td></tr>\n";

      print "           <TR bgColor=#99bcd8><TD colspan=2 align=left><font color=\"white\"><b>MENU</b></font></TD></TR>\n";
      print "           <TR><TD align=left><a href=\"main2.cgi?curdir=\"><img src=\"../image/landmark.png\" border=0> Main</a></TD>\n"; 
	  print "           <TD align=left><a href=\"main2.cgi?curdir=/Users/$usrid\"><img src=\"../image/home.png\" border=0> Home</a></TD></TR>\n";	  	  
	  print "           <TR><TD align=left><a href=\"task2.cgi\"><img src=\"../image/task.png\" border=0> Task</a></TD>\n";
      print "           <TD align=left><a href=\"YaBB_2.5.2/cgi-bin/yabb2/YaBB.pl?board=rfp\"><img src=\"../image/auction.png\" border=0> RFP</a></TD></TR>\n";		
      print "           <TR><TD align=left><a href=\"YaBB_2.5.2/cgi-bin/yabb2/YaBB.pl\"><img src=\"../image/bulletin_board.png\" border=0> Board</a></TD>\n";	  		    		  
      print "           <TD align=left><a href=\"YaBB_2.5.2/cgi-bin/yabb2/YaBB.pl?action=search\"><img src=\"../image/Find.png\" border=0> Search</a></TD></TR>\n";	  
      print "           <TR><TD align=left><a href=\"m.main2.cgi?curdir=\"><img src=\"../image/iphone.png\" border=0> Mobile</a></TD>\n";	  		  
      print "           <TD align=left><a href=\"help2.cgi\"><img src=\"../image/help_book.png\" border=0> Help</a></TD></TR>\n";	  

      print "           <tr><td colspan=2 height=8 bgcolor=EAF9FF></td></tr>\n";

      print "           <TR bgColor=#99bcd8><TD colspan=2 align=left><font color=\"white\"><b>INFO</b></font></TD></TR>\n";
      print "           <TR><TD colspan=2><br></TD></TR>\n";

      print "       </TABLE>\n";
      print "       </FORM>\n";
      print "     </td>\n";
      print "     <td width=8><br></td>\n";
      print "     <TD valign=top bgColor=#dbe6e0>\n";
      print "       <TABLE cellSpacing=0 cellPadding=4 width=100% border=0>\n";

	$_ = $FORM{"curdir"};
	s/\//\/<wbr>/g;
	
		$curdirl = "home$FORM{\"curdir\"}";
	
		my(@usrpathfi1c) = split(/,/, $usrpathf{$usrid});	
	
		my($usrpathfifg2) = 0;		
		
		foreach $usrpathfi2 (@usrpathfi1c)
		{	
			next if (!($curdirl =~ $usrpathfi2 && $usrpathfi2 ne ""));
				
			$usrpathfifg2 = 1;
			last;
		}			
		
      print "       <tr bgColor=#99bcd8><td style='width:560;text-wrap:hard-wrap ' colspan=2><font color=\"white\">/home$_/<wbr>$FORM{\"task\"}</font></td></tr>\n";
	  print "       <tr><td align=left><a href=\"javascript:history.go(-1)\"><img src=\"../image/GreenBack.png\" border=0></a></td><td align=right>\n";

			print "		<a href=\"javascript:history.go(0)\"><img src=\"../image/arrow_undo.png\" title=\"undo\" border=0></a> \n";	  
	  
	  if (($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) && ($usrpathfifg2 == 1)){

	  		print "	  	<a href=\"view2.cgi?curdir=$FORM{\"curdir\"}&task=$FORM{\"task\"}&action=editfile\"><img src=\"../image/gtk_edit.png\" title=\"edit\" border=0></a> \n";	  
			print "		<a href=\"view2.cgi?curdir=$FORM{\"curdir\"}&task=$FORM{\"task\"}&action=sharefile\"><img src=\"../image/page_gear.png\" title=\"property\" border=0></a> \n"; 		
			print "		<a href=\"file2.cgi?curdir=$FORM{\"curdir\"}&task=$FORM{\"task\"}&action=copyfile\"><img src=\"../image/copy.png\" title=\"copy\" border=0></a> \n"; 						
			print "		<a href=\"file2.cgi?curdir=$FORM{\"curdir\"}&task=$FORM{\"task\"}&action=renamefile\"><img src=\"../image/rename.png\" title=\"rename\" border=0></a> \n"; 		
			print "		<a href=\"file2.cgi?curdir=$FORM{\"curdir\"}&task=$FORM{\"task\"}&action=movefile\"><img src=\"../image/move.gif\" title=\"move\" border=0></a> \n"; 			
			print "		<a href=\"file2.cgi?curdir=$FORM{\"curdir\"}&task=$FORM{\"task\"}&action=delfile\"><img src=\"../image/trash.png\" title=\"delete\" border=0></a>\n";
	  }

	  print "     </td></tr>\n";
	  
	my($curdir) = $FORM{"curdir"};
	my($filename) = $FORM{"task"};
	my($action) = $FORM{"action"};	  

	if ($action eq "sharefile") {
			
		if (!(-e "home$curdir/\.attr\.$filename")) {
			open(SHA, ">home$curdir/\.attr\.$filename") || die $!;
			close SHA;
		}
	
	  	open(FLE, "home$curdir/\.attr\.$filename") || die $!;
		
		print "<tr><td align=left colspan=2>\n";
		print "<form method=POST action=\"file2.cgi\">\n";	
		
		print "<input type=\"hidden\" name=\"curdir\" value=\"$curdir\">\n";
		print "<input type=\"hidden\" name=\"program\" value=\"/home$curdir/$filename\">\n";
		print "<input type=\"hidden\" name=\"task\" value=\"$filename\">\n";
			
#		print "<a href=\"home$curdir/$filename\"><br>$filename</a><br>\n";
		print "add or remove users allowed to edit the file, one line per user.<br>\n";
		
		if ($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) {		
			print "<textarea name=\"source\" rows=5 wrap=off>\n";
		}
		else {
			print "<textarea readonly name=\"source\" rows=5 wrap=off>\n";		
		}
		
		foreach $line (<FLE>)
		{
			print "$line";
		}

		print "</textarea><p>\n";
		
		if ($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) {
			print "<input type=\"hidden\" name=\"saveas\" value=\"$filename\" size=\"40\">\n";
			print "<input type=\"submit\" name=\"action\" value=\"savefileattr\" size=\"\"><BR>\n";
		}	
		
		print "</form>\n";

		print "</td></tr>\n";

		close(FLE);

		print "       </table>\n";
		print "     </td>\n";
		print "  </tr>\n";
		print "</Table><br>\n";

		print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br>All Rights Reserved</td></tr>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br></td></tr>\n";
		print "</table>\n";
		print "</center>\n";

		print "</body></html>\n";
	}
	elsif ($action eq "sharefolder") {
			
		if (!(-e "home$curdir/\.sharefolder")) {
			open(SHA, ">home$curdir/\.sharefolder") || die $!;
			close SHA;
		}
	
	  	open(FLE, "home$curdir/\.sharefolder") || die $!;
		
		print "<tr><td align=left colspan=2>\n";
		print "<form method=POST action=\"file2.cgi\">\n";	
		
		print "<input type=\"hidden\" name=\"curdir\" value=\"$curdir\">\n";
		print "<input type=\"hidden\" name=\"program\" value=\"/home$curdir/sharefolder\">\n";
		print "<input type=\"hidden\" name=\"task\" value=\"sharefolder\">\n";
			
#		print "<a href=\"home$curdir/sharefolder\"><br>sharefolder</a><br>\n";
		print "add or remove users allowed to view this folder, one line per user.<br>\n";
		
		if ($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) {		
			print "<textarea name=\"source\" rows=5 wrap=off>\n";
		}
		else {
			print "<textarea readonly name=\"source\" rows=5 wrap=off>\n";		
		}
		
		foreach $line (<FLE>)
		{
			print "$line";
		}

		print "</textarea><p>\n";
		
		if ($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) {
#			print "save as<font color=#dbe6e0></font>: <input type=\"text\" name=\"saveas\" value=\"sharefolder\" size=\"40\">\n";
			print "<input type=\"submit\" name=\"action\" value=\"savefolderattr\" size=\"\"><BR>\n";
		}	
		
		print "</form>\n";

		print "</td></tr>\n";

		close(FLE);

		print "       </table>\n";
		print "     </td>\n";
		print "  </tr>\n";
		print "</Table><br>\n";

		print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br>All Rights Reserved</td></tr>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br></td></tr>\n";
		print "</table>\n";
		print "</center>\n";

		print "</body></html>\n";
	}	
	else {
#	  if (($filename =~ /\.htm$/i || $filename =~ /\.html$/i || $filename =~ /\.php$/i) && $action ne "editfile") {
	  if (($filename =~ /\.htm$/i || $filename =~ /\.html$/i) && $action ne "editfile") {	
		print "<tr bgcolor=eedad1><tr><td colspan=4 align=center><iframe width=\"100%\" height=\"600\" scrolling=\"auto\" frameborder=\"0\" src=\"http://scriptsmax.com/casper2/home$curdir/$filename\"></iframe></td></tr>\n";

		print "       </table>\n";
		print "</Table><br>\n";

		print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br>All Rights Reserved</td></tr>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br></td></tr>\n";
		print "</table>\n";
		print "</center>\n";
	  }
	  elsif ($filename =~ /\.pdf$/i) {
	
		print "<tr bgcolor=eedad1><tr><td colspan=4 align=center><iframe width=\"100%\" height=\"600\" scrolling=\"auto\" frameborder=\"0\" src=\"http://scriptsmax.com/casper2/home$curdir/$filename\"></iframe></td></tr>\n";

		print "       </table>\n";
		print "</Table><br>\n";

		print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br>All Rights Reserved</td></tr>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br></td></tr>\n";
		print "</table>\n";
		print "</center>\n";
	  }	  
	  elsif ($filename =~ /\.jpg$/i || $filename =~ /\.jpeg$/i || $filename =~ /\.png$/i || $filename =~ /\.gif$/i) {
	
		print "<tr bgcolor=eedad1><tr><td colspan=4 align=center><img src=\"http://scriptsmax.com/casper2/home$curdir/$filename\"></td></tr>\n";

		print "       </table>\n";
		print "</Table><br>\n";

		print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br>All Rights Reserved</td></tr>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br></td></tr>\n";
		print "</table>\n";
		print "</center>\n";
	  }	
	  elsif ($filename =~ /\.par$/i) {
	
	    open(FLE, "home$curdir/$filename") || die $!;
		
		print "<tr><td align=left colspan=2>\n";
		print "<form method=POST action=\"file2.cgi\">\n";
		print "<input type=\"hidden\" name=\"curdir\" value=\"$curdir\">\n";
		print "<input type=\"hidden\" name=\"program\" value=\"/home$curdir/$filename\">\n";
		print "<input type=\"hidden\" name=\"task\" value=\"$filename\">\n";

		print "<a href=\"home$curdir/$filename\"><br>$filename</a><br>\n";

		print "<textarea name=\"source\" rows=30 wrap=off>\n";
		
		foreach $line (<FLE>)
		{
			print "$line";
		}

		print "</textarea><p>\n";
		
		if ($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) {
			print "save as<font color=#dbe6e0></font>: <input type=\"text\" name=\"saveas\" value=\"$filename\" size=\"40\">\n";
			print "<input type=\"submit\" name=\"action\" value=\"savepar\" size=\"\"><BR>\n";
		}	
	
		print "</form>\n";

		print "</td></tr>\n";

		close(FLE);

		print "       </table>\n";
		print "     </td>\n";
		print "  </tr>\n";
		print "</Table><br>\n";

		print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br>All Rights Reserved</td></tr>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br></td></tr>\n";
		print "</table>\n";
		print "</center>\n";

		print "</body></html>\n";
      }	
	  elsif($filename =~ /\.sas$/i || $filename =~ /\.r$/i) {
	
	    open(FLE, "home$curdir/$filename") || die $!;
		
		if ($filename =~ /\.sas$/i || $filename =~ /\.r$/i) {
			print "<tr><td align=left colspan=2>\n";
			print "<form method=POST action=\"exec2.cgi\">\n";
			print "<input type=\"hidden\" name=\"curdir\" value=\"$curdir\">\n";
			print "<input type=\"hidden\" name=\"program\" value=\"/home$curdir/$filename\">\n";
			print "<input type=\"hidden\" name=\"task\" value=\"$filename\">\n";
		}
		else {
			print "<tr><td align=left colspan=2>\n";
			print "<form>\n";			
		}
		
		print "<a href=\"../home$curdir/$filename\"><br>$filename</a><br>\n";

			my($allowedit) = 0;	
			
			if ($usrtypef{$usrid} == 0) {
				$allowedit = 1;
			}
			elsif ("home$curdir" =~ /home\/Users\/$usrid/){
				$allowedit = 1;
			}
			elsif (-e "home$curdir/\.attr\.$filename") {
			
				open(SHA, "home$curdir/\.attr\.$filename") || die $!;
			
				foreach $ln (<SHA>) {
				
					$ln =~ s/^\s+|\s$//g;
					
					if (lc($ln) eq $usrid || lc($ln) eq "all") {						
						$allowedit = 1;
					}
				}
				
				close(SHA);	
			}
			else {
				$allowedit = 0;
			}		
		
		if ($filename =~ /\.sas$/i || $filename =~ /\.r$/i) {	
			if (($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) && ($usrpathfifg2 == 1 or $allowedit == 1)){
#			if (($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) && ($allowedit == 1)){
				print "<textarea name=\"source\" rows=30 wrap=off>\n";
			}
			else {
				print "<textarea readonly name=\"source\" rows=30 wrap=off>\n";			
			}
		}
		else {
			if ($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) {		
				print "<textarea rows=30 wrap=off>\n";
			}
			else {
				print "<textarea readonly rows=30 wrap=off>\n";			
			}
		}
		
		foreach $line (<FLE>)
		{
			print "$line";
		}

		print "</textarea>\n";
		
		if ($filename =~ /\.sas$/i || $filename =~ /\.r$/i) {
			print "<p><input type=\"submit\" name=\"action\" value=\"run\" size=\"\">\n";
			
			if (($usrpathfifg2 == 1 or $allowedit == 1) && ($usrtypef{$usrid} < 2)) {
#			if (($allowedit == 1) && ($usrtypef{$usrid} < 2)) {
				
				print "<input type=\"reset\" name=\"action\" value=\"reset\" size=\"\"><p>\n";
				print "\n";
				print "save as<font color=#dbe6e0></font>: <input type=\"text\" name=\"saveas\" value=\"$filename\" size=\"40\">\n";
				print "<input type=\"submit\" name=\"action\" value=\"save\" size=\"\"><BR>\n";
			}	
		}		
		
		print "</form>\n";

		print "</td></tr>\n";

		close(FLE);

		print "       </table>\n";
		print "     </td>\n";
		print "  </tr>\n";
		print "</Table><br>\n";

		print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br>All Rights Reserved</td></tr>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br></td></tr>\n";
		print "</table>\n";
		print "</center>\n";

		print "</body></html>\n";
      }
	  elsif ($filename =~ /\.msg$/i) {
	
	    open(FLE, "home$curdir/$filename") || die $!;
		
		print "<tr><td align=left colspan=2>\n";
		print "<form method=POST action=\"file2.cgi\">\n";
		print "<input type=\"hidden\" name=\"curdir\" value=\"$curdir\">\n";
		print "<input type=\"hidden\" name=\"program\" value=\"/home$curdir/$filename\">\n";
		print "<input type=\"hidden\" name=\"task\" value=\"$filename\">\n";

		print "<a href=\"home$curdir/$filename\"><br>$filename</a><br>\n";

		print "<textarea readonly name=\"source\" rows=26 wrap=off>\n";
		
		foreach $line (<FLE>)
		{
			print "$line";
		}

		print "</textarea>\n";
		print "<br>your message:\n";
		print "<textarea name=\"append\" rows=4 wrap=off>\n";
		
		print "</textarea><p>\n";
		
		if ($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) {
			print "<font color=#dbe6e0></font><input type=\"hidden\" name=\"saveas\" value=\"$filename\" size=\"40\">\n";
			print "<input type=\"submit\" name=\"action\" value=\"savefeedback\" size=\"\"><BR>\n";
		}	
	
		print "</form>\n";

		print "</td></tr>\n";

		close(FLE);

		print "       </table>\n";
		print "     </td>\n";
		print "  </tr>\n";
		print "</Table><br>\n";

		print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br>All Rights Reserved</td></tr>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br></td></tr>\n";
		print "</table>\n";
		print "</center>\n";

		print "</body></html>\n";
      }		
	  else {
	
		open(FLE, "home$curdir/$filename") || die $!;
		
		print "<tr><td align=left colspan=2>\n";
		print "<form method=POST action=\"file2.cgi\">\n";	
		
		print "<input type=\"hidden\" name=\"curdir\" value=\"$curdir\">\n";
		print "<input type=\"hidden\" name=\"program\" value=\"/home$curdir/$filename\">\n";
		print "<input type=\"hidden\" name=\"task\" value=\"$filename\">\n";
			
		print "<a href=\"home$curdir/$filename\"><br>$filename</a><br>\n";
				
			my($allowedit) = 0;	
			
			if ($usrtypef{$usrid} == 0) {
				$allowedit = 1;
			}
			elsif ("home$curdir" =~ /home\/Users\/$usrid/){
				$allowedit = 1;
			}
			elsif (-e "home$curdir/\.attr\.$filename") {
			
				open(SHA, "home$curdir/\.attr\.$filename") || die $!;
			
				foreach $ln (<SHA>) {
				
					$ln =~ s/^\s+|\s$//g;
					
					if (lc($ln) eq $usrid || lc($ln) eq "all") {						
						$allowedit = 1;
					}
				}
				
				close(SHA);	
			}
			else {
				$allowedit = 0;
			}				
		
		if (($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) && ($usrpathfifg2 == 1 or $allowedit == 1)){
#		if ($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) {		
			print "<textarea name=\"source\" rows=30 wrap=off>\n";
		}
		else {
			print "<textarea readonly name=\"source\" rows=30 wrap=off>\n";		
		}
		
		my($linecnt)= 0;
		
		foreach $line (<FLE>)
		{
			print "$line";
			
			$linecnt++;
			
			if ($linecnt > 2000) {
				print "\nwarning: file exceeds 2000 lines, right click link to download.\n";
				last;
			}
		}

		print "</textarea><p>\n";
		
		if ($usrtypef{$usrid} == 0 or $usrtypef{$usrid} == 1) {
			print "save as<font color=#dbe6e0></font>: <input type=\"text\" name=\"saveas\" value=\"$filename\" size=\"40\">\n";
			print "<input type=\"submit\" name=\"action\" value=\"save\" size=\"\"><BR>\n";
		}	
		
		print "</form>\n";

		print "</td></tr>\n";

		close(FLE);

		print "       </table>\n";
		print "     </td>\n";
		print "  </tr>\n";
		print "</Table><br>\n";

		print "<table cellspacing=0 cellpadding=0 width=100% border=0>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br>All Rights Reserved</td></tr>\n";
		print "    <tr><td bgcolor=#dbe6e0 align=center><br></td></tr>\n";
		print "</table>\n";
		print "</center>\n";

		print "</body></html>\n";
      }	
	}  
  }
}
