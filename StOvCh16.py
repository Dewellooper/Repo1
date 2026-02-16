__version__ = "260216_2115"

#234+6789!#234+6789!#234+6789!#234+6789!#234+6789!#234+6789!#234+6789!72
########################################################################

Prj_name="""StackOverflow - \
Challenge #16
Deadline is March 11, 2026"""

#breakpoint()

#(Nominalwert) face amount, face value of a coin
#fraction consists of numerator(Zähler) and denominator (Nenner)


import argparse
import logging
#import re		#the built-in str.replace() is powerful enough
import sys


print(f"{Prj_name}\nVersion {__version__}\n")

set_cmdline_args_internal = (len(sys.argv)<2 ) #no cmdLine args/options
if set_cmdline_args_internal:
#######################################################################
# Config command line options here, but cmd_line has priority
#######################################################################
#
#	uncomment your chooise
#		don't remove leading tab

#	set_cmdlineArgs=['-h']				# help screen and quit
#	set_cmdlineArgs=['-d']				# debug with pdb
	set_cmdlineArgs=['-m']				# MarkDown table line
#	set_cmdlineArgs=['-t']				# Test
#	set_cmdlineArgs=[]		
	

#######################################################################

else:		#opt. in cmd line exist 
	set_cmdlineArgs=[]


### L I T T L E   H E L P E R  ###
NL = '\n'
#RepLvl= 0	#Report level option -v VERBOSE
#show_report_level = False			#set True with option -s

DATA_test = [ [[1, 5, 10], [10, 2, 1], 23]	]	#10+5+5+1+1+1 = 23
DATA = \
[
  [[1],[100],73],
  [[1,5],[3,2],14],
  [[1,5,10],[10,2,1],23],
  [[2,4],[10,10],7],
  [[3,7],[10,10],24],
  [[1,3,4],[5,5,1],6],
  [[1,5,10],[2,1,1],18],
  [[1,7,10],[10,1,1],14],
  [[4,5,9],[5,5,5],18],
  [[6,9,20],[5,5,5],43],
  [[5,10],[0,10],50],
  [[1,2,5],[0,0,10],10],
  [[7],[3],21],
  [[7],[2],21],
  [[1,3,5],[1,1,1],8],
  [[1,2,5,10],[1,1,1,1],18],
  [[2,3,7],[10,10,1],14],
  [[1,4,6,9],[2,2,2,2],18],
  [[5,11,17],[10,10,10],34],
  [[1,8,15],[100,1,1],23],
  [[1,2],[10,5],7],
  [[1,3],[5,2],8],
  [[2,5],[5,2],12],
  [[1,4,6],[5,1,1],10],
  [[1,3,9],[3,1,1],13],
  [[2,7,10],[5,1,1],17],
  [[1,2,5,10],[3,2,1,1],18],
  [[1,3,5],[2,2,1],11],
  [[1,2,5],[10,1,1],8],
  [[1,2,5,10],[10,2,1,1],19],
  [[3,4,7],[5,2,1],15],
  [[2,5,10],[3,2,1],20],
  [[1,2,3],[5,5,5],9],
  [[1,3,4,5],[2,2,1,1],12],
  [[2,3,5,8],[3,2,2,1],18],
  [[1,5,6],[5,2,1],14],
  [[1,2,4],[3,3,1],9],
  [[1,3,7],[2,2,1],10],
  [[2,4,6],[2,2,1],12],
  [[1,2,5],[1,1,1],7],
  [[3,5,8],[2,1,1],13],
  [[1,2,6],[3,1,1],8],
  [[2,3,5],[5,2,2],14],
  [[1,4,7],[3,1,1],12],
  [[1,3,6,9],[2,2,1,1],15],
  [[2,5,7],[1,1,1],10],
  [[1,2,5,10],[2,2,1,1],19],
  [[1,3,5,8],[3,2,2,1],17],
  [[2,4,6,9],[2,2,1,1],18],
  [[1,2,3,7],[3,2,1,1],13],
  [[1,3,5],[5,3,2],16],
  [[2,5,10],[2,1,1],17],
  [[1,4,6],[3,1,1],11],
  [[1,2,5],[10,1,1],14],
  [[3,7,11],[2,1,1],18],
  [[1,2,3,4],[2,2,2,1],9],
  [[1,5,10,20],[5,2,1,1],23],
  [[2,3,5,7],[2,2,1,1],15],
  [[1,4,5,6],[3,1,1,1],13],
  [[1,2,3,6],[2,2,1,1],10],
  [[1,3,5,9],[3,2,1,1],16],
  [[2,4,7,10],[2,1,1,1],18],
  [[1,2,5,8],[5,2,1,1],19],
  [[1,3,6,7],[2,2,1,1],14],
  [[1,2,4,5],[3,2,1,1],12],
  [[3,5,7,9],[2,1,1,1],15],
  [[1,2,3,5],[4,2,1,1],11],
  [[1,4,6,8],[2,2,1,1],16],
  [[2,3,5,9],[3,2,1,1],14],
  [[1,2,5,6],[3,2,1,1],13],
  [[1,3,4,7],[2,2,1,1],12],
  [[2,4,6,8],[2,2,1,1],14],
  [[1,2,3,7],[3,2,1,1],13],
  [[1,3,5,7],[2,2,1,1],12],
  [[2,4,5,9],[3,2,1,1],15],
  [[1,2,4,6],[2,2,1,1],11],
  [[1,3,5,8],[3,2,1,1],14],
  [[2,3,6,7],[2,2,1,1],13],
  [[1,2,5,10],[4,2,1,1],17],
  [[1,3,6,9],[3,2,1,1],15],
  [[2,5,7,10],[2,1,1,1],16],
  [[1,2,3,4],[5,2,1,1],12],
  [[1,3,5,6],[3,2,1,1],14],
  [[2,4,6,9],[2,2,1,1],15],
  [[1,2,3,7],[3,2,1,1],12],
  [[1,4,5,8],[2,2,1,1],14],
  [[2,3,5,7],[2,2,1,1],13],
  [[1,2,4,6],[3,2,1,1],15],
  [[1,3,5,9],[2,2,1,1],14],
  [[2,5,7,10],[2,1,1,1],17],
  [[1,2,3,6],[3,2,1,1],13],
  [[1,3,4,7],[2,2,1,1],12],
  [[2,4,6,8],[2,2,1,1],14],
  [[1,2,5,8],[3,2,1,1],15],
  [[1,3,6,9],[3,2,1,1],16],
  [[2,3,5,9],[2,2,1,1],15],
  [[1,2,3,4],[4,2,1,1],11],
  [[1,3,5,7],[2,2,1,1],13],
  [[2,4,6,9],[2,2,1,1],14],
  [[1,2,5,6],[3,2,1,1],12]
]

## Little helper ## print_output
def print_output(line, headline=False):
	global clArg

	if clArg.markDown:
		line  = '|'+ line.replace('\t', ' | ') + '|'
	print(line)

	if headline and clArg.markDown:
		cols = max(line.count('\t'), line.count('|'))-1
		print('|' + cols * ' --- |')
## Little helper ## END print_output


def chk_asc_denomi(a):
	#check, if denom. are in ascending order
	for i in range(len(a[0])-1):
		if a[0][i] > a[0][i+1]:
			return False
	return True		##okay
## Little helper ## END chk_asc_denomi

def sum_all_coins(d,c):
	def fu(den, n):
		return den * n
		
	m= map(fu, d, c)            #sum_all_coins(a[0],a[1])
	return sum(m)
## Little helper ## END sum_all_coins_pro_example



## Little helper ##  get_args()
def get_args():
	global DATA
	
	ap = argparse.ArgumentParser(description= Prj_name, \
		 epilog="Find minimal coins to pay a value. " )
	
	ap.add_argument("-d", "--debug",	\
			action = "store_true", \
			help = "starts Pdb.breakpoint() after Cmd_Line_Parsing")


	ap.add_argument("-m", "--markDown",	\
			action = "store_true", \
			help = "output as markdown table")


	ap.add_argument("-t", "--test",	\
			action = "store_true", \
			help = "Test with the example in challenge description")

	if set_cmdlineArgs:			#Options & Args in source code
		ns = ap.parse_args(set_cmdlineArgs)
	else:
		ns = ap.parse_args()	#Options & Args from CmdLine
		
	if ns.test:
		DATA = DATA_test	
		
	return ns	
## Little helper ## END get_args()

def get_solution(a):

	d = denominators = a[0]
	c = counts		 = a[1]
	t = target		 = a[2]
	s = selected	 = [0 for i in range(len(c))]
	
	
	
	sv=	sum_all_coins(d, s)		#value of selected
	eq= ''	#equation  10+10-10+5
	
	for i in range(len(s)-1, -1, -1):
		eq += '+' + str(i)
		print(f"------>{i}, {eq}")
	
	
		while sv < t :
			pass
			break
	#	end while
	
#	end for	
	
	
	
		
#	how_many_coins = sum(s)
	return (sum(s), sv)
## END of get_solution()

def main():
	global clArg
	clArg = get_args()
	if clArg.debug: 
		breakpoint()
		
	l_chk1=[]
	result = [0 for i in range(100)	]

	line = f"{' #'}	{'denominator'!s:15}	{'count of coins'!s:15}"+\
	f"	{' $':2}	{'chk':4}	{'($)':3}	{'cnt':3}	{'comment'}"

	print_output(line, headline=True)

	for n,a in enumerate(DATA):
		check1 = chk_asc_denomi(a)
		l_chk1.append(check1)
		
		sum1   = sum_all_coins(a[0], a[1])
		if sum1 >= a[2]:
		
			result[n], msg = get_solution(a)	#"enough"
		else:
			msg = "not enough coins!!!"
			result[n] = -1

		line = f"{n:2d}	{a[0]!s:15}	{a[1]!s:15}	{a[2]:2d}	" +\
			   f"{check1}	{sum1:3d}	{result[n]:3d}	{msg}"
		print_output(line)
		
	if all(l_chk1):
		print(f"\nall denominators are in ascending order sorted.\n"+\
			f"\tSo we don't have to sort they.")	
	else:
		print(f"some denominators are not in ascending order sorted.")

### END main()

if __name__ == "__main__": 
	main()