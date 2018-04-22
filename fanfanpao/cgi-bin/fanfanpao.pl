#!/usr/bin/perl
##
##  cspr -- Perl program that executes submitted sas jobs
##

use File::Copy;
use Fcntl;

#######################
# Handle Error

sub error {
   print "error... $! \n";
}

#######################
# Main Loop

while (1 == 1) {

    open (LOCK, ">/home/user/Downloads/git/SAS-Batch-Submit-Server/fanfanpao/lock.xml") || die $!;

    if (flock(LOCK,2)) {

	open(TASKREAD, "/home/user/Downloads/git/SAS-Batch-Submit-Server/fanfanpao/task.xml") || die $!;

	@alltasks = <TASKREAD>;

	my($zzdev, $zzino, $zzmode, $zznlink, $zzuid, $zzgid, $zzrdev, $zzsize, $zzatime, $zzmtime, $zzctime, $zzblksize, $zzblocks) = stat(TASKREAD);
	
	my($zysec, $zymin, $zyhour, $zyday, $zymon, $zyyear, $zywday, $zyyday, $zyisdst) = localtime($zzmtime);	

	$zyyear =$zyyear%100;

  	if ($zysec < 10) { $zysec = "0$zysec";}
   	if ($zymin < 10) { $zymin = "0$zymin";}
   	if ($zyhour < 10) { $zyhour = "0$zyhour";}
   	if ($zyday < 10) { $zyday = "0$zyday";}
	$zymon =$zymon + 1;
   	if ($zymon < 10) { $zymon = "0$zymon";}
   	if ($zyyear < 10) { $zyyear = "0$zyyear";}

	close(TASKREAD);

	$basedir = "/home/user/Downloads/git/SAS-Batch-Submit-Server/fanfanpao";

	open(TASK, ">$basedir/task.xml") || die $!;

	my($linecount) = 0;
	my($taskflag) = 0;
	my($line1);

	foreach $line (@alltasks) {
	  		$linecount++;

	   	if ($linecount == 1) {
			$line1 = $line;
			chop($line);
			($taskcount, $user, $softw, $upath, $cmnd) = split(/:/,$line);

			$wpath = $upath;
			#$wpath =~ tr/\//\\/;

              	($sasexe, $noautoexec, $sysin, $program, $log, $logfile, $print, $printfile) = split(/ /,$cmnd); 
			$taskflag = 1;
	   	}
	   	else {
			print TASK $line;
	   	}
	}
	close(TASK);

	if ($taskflag == 1) {

			open(BUSY, ">$basedir/busy.xml") || die $!;
			print BUSY $line1;
        		close(BUSY);

			($ppath, $prog) = $program =~ m|^(.*[\/])([^/\/]+?)$|;
			
			#$program =~ tr/\//\\/;

			printf "$program \n";

			copy("$basedir$program", "../$prog") || die $!;

			$sasexe = "sas941";
			$prog1 = "../$prog";
			$logfile1 = "../$logfile";
			$printfile1= "../$printfile";

			$cmnd1 = "$sasexe $noautoexec $sysin $prog1 $log $logfile1 $print $printfile1";

			printf "$cmnd1 \n";

			move("$basedir/parm$taskcount.xml", "parm.xml");

			flock(LOCK, 8);
    			close (LOCK);

			system($cmnd1);

			if (-e "$prog1") {
				unlink "$prog1";
			}

			move($logfile1, "$basedir/$wpath/$logfile");
			move($printfile1, "$basedir/$wpath/$printfile");

			#die ("End");
			
#			my @ssds = glob "*.sas7bdat";
			
#			foreach my $ssd (@ssds) {
#				move($ssd, "$basedir\\$wpath");
#			}
			
			if (-e $prog) {
				unlink $prog;
			}

			if (-e "parm.xml") {
				unlink "parm.xml";
			}

			open(HIST, ">>$basedir/hist.xml") || die $!;
			print HIST "$zyyear-$zymon-$zyday $zyhour:$zymin:$zysec $user:/$upath> $cmnd\n";
			close(HIST);

			if (-e "$basedir/busy.xml") {
				unlink "$basedir/busy.xml";
			}
		}
		else {
			flock(LOCK, 8);
    			close (LOCK);
		}

  	}
	else {
    		close (LOCK);
	}

  	sleep(10);

}

