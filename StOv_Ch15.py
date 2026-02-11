__version__ = "260211_0815"
Prj_name="""StackOverflow - \
Challenge #15
Deadline is February 11, 2025"""

#breakpoint()
''' #setting the command line args 
		in source code for using
		in http://mimo.org 
'''

import argparse
import re
import sys
import textwrap

set_cmdline_args_internal = (len(sys.argv)<2 ) #no cmdLine args / options
if set_cmdline_args_internal:
##########################################################################
# Config command line options here, but cmd_line has priority
##########################################################################
#
#	uncomment your chooise
#		don't remove leading tab

#	set_cmdlineArgs=['-h']				# help screen and quit
	set_cmdlineArgs=['-v 32']			# solution only
#	set_cmdlineArgs=['-vMax', '-s']		# Max output, show_report_level
#	set_cmdlineArgs=['-vMax', '-d']				# debug with pdb
	

##########################################################################

else:		#opt. in cmd line exist 
	set_cmdlineArgs=[]


### L I T T L E   H E L P E R  ###
NL = '\n'
RepLvl= 0	#Report level option -v VERBOSE
show_report_level = False			#set True with option -s
pat_rl = re.compile("rl\(\s*(\d+)")
rl_max = 0		#set in find_max_used_report_level 
				# by scanning source
## Little Helper ## report level
def rl(n, with_headline = True):		
	def bits_set_on(n):
		repLvl01 = RepLvl
		ret = ""
		bit_pos = 0
		while repLvl01 > 0:
			if  repLvl01 % 2:
				ret = f"+{2 ** bit_pos}" + ret
			repLvl01 //= 2
			bit_pos += 1
		return ret[1:]  #without the leading "+"

	ret = bool(RepLvl & 2**n)
	if ret:
		on_off="ON" 
	else:on_off="OFF"
	
	p5 = ". "*5
	bso = bits_set_on(n)
	if show_report_level and with_headline:
		print( f"\n{p5}report level -v {RepLvl}={bso} " +\
			f" {2**n}= 2**{n} ", on_off , p5)
	return ret

## Little Helper ## find max used report level rl(?)
## for option -h to show, what -v VERBOSEmax is poosible 
def find_max_used_report_level():
	#*** Impove: topics of all rl()
	#		1 = cl_Arg_Namespace
	#		...
	def sort_by_rl(line):
		rl_call = pat_rl.search(line)
		if rl_call:
			return int(rl_call.group(1))
		else:
			return -1
			
	rl_max = 0
	try:
		fd= open(__file__, mode="r")
		src = fd.read().split(NL)		
	except:
		print(f"Can't open/ read source file {__file__}")
		quit()
		
	msg = ""
	for k, i in enumerate(src):
		rl_call = pat_rl.search(i)
		if rl_call:
			rl_arg = int(rl_call.group(1))
			msg += f"Line {k+1:3d}: {textwrap.dedent(i)}\n"
			rl_max = max(rl_max, rl_arg)
			
	if rl(6):				###descr. already used rl()-numbers
		
		print(f"sorted by line number\n{msg}")
		l_msg = msg.split(NL)
		l_msg.sort(key=sort_by_rl)
		msg = (NL).join( l_msg )
		print(f"\nsorted by report number\n{msg}")
	
				
	if rl(7):				###descr. count source lines
		print(f"Lines in source file {len(src)}")
		
	return rl_max
## Little Helper ## END of find max used report level rl(?)
## Little Helper ## end
	
#############################
### C L A S S declaration ###
#############################
class Doc:
	def __init__(self, document):
		self.words = document				#given sorted list of SELF.words
		
	# count all words	
		self.wordsN = len(self.words)		#
		
	# how many different characters
		self.chars = self.find_all_used_chars()

	# different letters	 old name=dif_ltr, new name charsN
		self.charsN = len(self.chars)


	#tupel (pre, succ)  predecessor, successor
		self.sequence_rules = self.generate_sequence_rules()

		if rl(1):				###descr. Sequence Rules
			print(f"Sequence Rules")
			for i,sr in enumerate(self.sequence_rules,1):
				print(f"{sr[0]}<{sr[1]} ", end='')
				if i % 16 == 0:
					print()
			print()
	#the first has no_predecessor
		self.alphabet = self.no_predecessor()

		self.greeks		= self.get_greeks()
		self.substitute	= self.get_substitute()
		
###class Doc ## END of __init__()

	def get_substitute(self):
		sub = []
		tg	= self.greeks			#translate symbol to greek letter
		for line in self.words:
			new_line = ""
			for ch in line:
				new_line += tg[ch]
			sub.append(new_line)
		return sub


	def get_greeks(self):
		gk = {}
		for n, sy in enumerate(self.alphabet):
			if n <= 16:
				gk[sy] = chr(n + 0x3b1)
			else:	
				gk[sy] = chr(n + 0x3b2)
		return gk		


	def no_predecessor(self):
		
		def sort_seq_rules(tps):		#tupel (pred., succ.)
			return tps[0] + tps[1]

		def sort_count_pre(ch):
			return count_predecessors[ch]

		#  all rules that rm_ch is predeseccor
		def remove_rules(rm_ch):
			i = 0
			while i < len(self.sequence_rules):
				if self.sequence_rules[i][0] == rm_ch:
					self.sequence_rules.pop(i)
				else:
					i += 1
			return len(self.sequence_rules)

		def remove_found_letter_in_cp_master(rm_ch):
			del count_predecessors_master[rm_ch]
			
	###no_predecessor()## starts here
		alphabet = []
		#to check, how the number of rules shrinks.
		l_rules = [self.wordsN, len(self.sequence_rules)]
		
# not nessesary to remove double rules. We are looking for an char,
#	that hasn't any predesessor.
#		len_sq_rules_without_doubles = remove_doubles_rules()
#		l_rules.append(len_sq_rules_without_doubles)	
		self.sequence_rules.sort(key=sort_seq_rules)
		

		count_predecessors_master = {}
		for ch in self.chars:
			count_predecessors_master[ch] = 0 

		#Messages are collected. So the output will not interupted
		# while running the analyse process
		msg3 = ''
		msg4 = ''

		while len(alphabet) < self.charsN:
		
	#		start with a new count dictionary in every loop
			count_predecessors = dict(count_predecessors_master)
			
			for sr in self.sequence_rules:
				count_predecessors[sr[1]] += 1
	
			lcp = list(count_predecessors)
			lcp.sort(key=sort_count_pre)
			only_one_has_no_pred = 0
				
			for ch in lcp:
				if count_predecessors[ch] == 0:
					rule_to_remove = ch
					only_one_has_no_pred += 1
				msg3  += ch + ' ' + str(count_predecessors[ch])
		
			if only_one_has_no_pred != 1:
				print(f"{'* '*10} ERROR more then one OR not any char" +\
					" hasn't a predecessor")
				quit()
			
			msg3  += NL	
			alphabet.append(rule_to_remove)
			l_rules.append(remove_rules(rule_to_remove))
			remove_found_letter_in_cp_master(rule_to_remove)
			msg4 += ''.join(str(l_rules)) + NL

		if rl(2):				###descr. find char without any predecessors
			print(f"count_predecessors sorted\n" + \
			"only one char shouldn't have any predecessor\n" \
			+f"{msg3}")
		if rl(3):				###descr. check shrinking the rules
			print(f"check shrinking the rules\n{msg4}")
		return alphabet
	###no_predecessor()## ends here


## Class declaration ## method

	def generate_sequence_rules(self):
		def pre_succ_tupel(i):
			pos = 0
			pos_max = min(len(self.words[i]), len(self.words[i+1]))
			
			#compare til the end of the shorter word
			while pos < pos_max:
				p,s = self.words[i][pos], self.words[i+1][pos]
				if p == s:
					pos += 1
					continue
				else:
					break
			return (p,s)
					
		sq_rules = []
		for i in range(self.wordsN-1):
			pst= pre_succ_tupel(i)
			if pst[0] != pst[1]:
				sq_rules.append(pst)
		return sq_rules
######################
# Discussion: Another word list could make here a contradiction.
# example:
#       out
#       outdoor
# the while loop is ending with ('t', 't')      
# the later search for next character without a predeseccor
# would not find a candidate, because 't' has hisself as pred.
# In our word list does not appear such a constellation.                                        
######################


## Class declaration ## method find_all_used_chars			
	def find_all_used_chars(self):
		chars = []
		for word in self.words:
			for ch in word:
				if ch not in chars:
					chars.append(ch)
		return chars
	## End of method find_all_used_chars
		
## Class declaration ## method status 
	## statistcs and the solution with 
	## the alphabet, we are looking for.
	def stat(self):
		return ({"wordsN": 			self.wordsN			,\
				 "characters":		self.charsN			,\
				 "alphabet":		self.alphabet		,\
				 "greeks":			self.greeks			,\
				})
## Class declaration ## end of class Doc()	


### D A T A F I L E  O P E N () ###
###################################
def datafileOpen(fn):
	try:
		fd = open(fn,'r')
		data = fd.read()
	except:
		print(f"Can not open data FILE {fn}")
		quit()
	fd.close()

	lines = data.split('\n')
	return lines

# C M D _ L I N E _ A R G S () ###
##################################
def cmd_line_args():
	global	RepLvl,	\
			show_report_level,	\
			rl_max
					
	ap = argparse.ArgumentParser(description= Prj_name, \
		epilog="Find the alphabet of an ordered word list, " +\
		"characters in UniCode. Use -v 32 to see only the solution ")
		
	ap.add_argument("-d", "--debug",	\
					action = "store_true", \
					help = "starts Pdb.breakpoint() after Cmd_Line_Parsing")
					
	deflt = 'StOv15_data.py'			
	ap.add_argument("-f", "--file", default=deflt, \
		help= "Filename contained data. Default is " + deflt)
		
	rl_max = find_max_used_report_level()
	ap.add_argument("-v", "--verbose", "--reportLevel",	\
					action = "store", default= 0, # type=int,		\
					help = "bitwise switched detailed output."+	\
					f"0 or not set = no details. Max= {2**(rl_max+1)-1}. " +\
					"using -vMax or -vAll to get all reports")

	ap.add_argument("-s", "--show_report_level", \
		action = "store_true")

	if set_cmdlineArgs:			#Options & Args in source code
		ns = ap.parse_args(set_cmdlineArgs)
	else:
		ns = ap.parse_args()	#Options & Args from CmdLine
	
	if ns.verbose.lower() in ['all', 'max']:
		RepLvl = 2**(rl_max+1)-1
	else:
		try:
			RepLvl = int(ns.verbose)
		except Exception as e:
			print(NL*3+f"{e}")
			print(f"Bad option -v VERBOSE {ns.verbose} not a number " + \
				   "btw the words 'max' or 'all'")
		
	show_report_level = ns.show_report_level		#option -s
	return ns
## cmd_line_args ## end

###############
### M A I N ###
###############
def main():
	print(f"{Prj_name}\nVersion {__version__}\n")
	clArg  = cmd_line_args()
	if rl(0):				###descr. Options & Args (source/ Cmd_Line)
		if set_cmdlineArgs:
			cla_src = "set in source: " + ' '.join(set_cmdlineArgs)
		else:	
			cla_src = "found in Cmd_Line"
		print(f"Options & Args ({cla_src} ) = \n{clArg}\n")
		
	if clArg.debug:
		breakpoint()
			
	d = Doc(datafileOpen(clArg.file))

	if rl(4):				###descr. class instance variables
		ds = d.stat()			#dict of status
		for k in ds:
			print(f"{k:20s}\t{ds[k]}")
			
		
	if rl(5):				###descr. ByteCodes UTF-8 character
		al = d.alphabet
		gk = d.greeks
		
		print("The solution: Alphabet AND UniCode AND byte code AND possible greek letter")
		print(f"in one row: {' '.join(al)}\n" +\
			  f"{al[:8]}\n{al[8:16]}\n{al[16:]}")
		for n, key in enumerate(al):
			print(f'{n:02d}\t{key} \\u{ord(key):04x} \t{key.encode()}' +\
				f"\t{gk[key]}")

		print()
		
	if rl(6, with_headline = False) or \
	   rl(7, with_headline = False):	###descr. devHelp find_max_used_report_level 
		find_max_used_report_level()
	if rl(8):				###descr. #translate symbol to greek letter
		for line in d.substitute:
			print(line)
			
	if rl(9):				###descr. #transscript greek symbol letter and translate 
		print(NL+"English translation")
		print("sorry, not ready yet")
      
## Main ## end	

if __name__ == "__main__": main()
