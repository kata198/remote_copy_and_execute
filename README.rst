remote\_copy\_and\_execute
==========================


remote\_copy\_and\_execute is a tool used to copy a script in batch to a set list of hosts, execute N at a time, and print the results.

It uses the SSH protocol (ssh and scp utilities) to perform the acts. This is useful for a multiude of purposes, 

from running custom audit scripts to deployment scripts, activation and really any batch task.


**Example Usage:**



	remote_copy_and_execute --rcae-at-a-time=3 --rcae-as-user=www --rcae-skip-bad-hosts ./myScriptName -- host1 host2 host3 host4 host5 host6 host7


The above command will copy and execute execute as "www" the script "myScriptName" on 3 hosts at a time, until all given hosts are completed or failed, and print results on completion.


	remote_copy_and_execute --rcae-batch --rcae-as-user=myuser /home/myuser/scripts/audit -- host1 host2 host3 host4

The above command will copy and execute execute "/home/myuser/scripts/audit" on all of the given hosts, as "myuser", using common batch options.


**All Options:**



	Usage: remote_copy_and_execute [program] [args] (--) [hostname1] [hostnameN]

	Copies a script and executes on multiple hosts simultaneously. Use "--" after the args and before the list of host names.

	Script must be executable by the running user


	remote_copy_and_execute arguments:

		\-\-rcae\-timeout=#seconds         to use a timeout.

		\-\-rcae\-omit\-empty               Omit printing empty results

		\-\-rcae\-at\-a\-time=#              Split application into given # chunks

		\-\-rcae\-hide\-date                Do not show runtime date

		\-\-rcae\-skip\-bad\-hosts           Skip bad hosts. Default is to terminate.

		\-\-rcae\-quiet                    Omit all output except that from the script. Implies hide-date

		\-\-rcae\-as\-user=username         Perform copy and execute as given user. Default is root.

		\-\-rcae\-print\-on\-host\-complete   Print right after each host completes execution. Default is to print at end of each set. Assumes rcae-hide-date.


		\-\-rcae-batch                    Sets defaults [listed below]. Sane defaults for batch
				                          executions. This directive is evaluated first, so you can override
				                          the ones that take a paramater.


					                        timeout=2

					                        omit-empty

					                        at-a-time=15

					                        hide-date

					                        skip-bad-hosts



		--rcae-help                     Show this message


