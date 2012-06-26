from pysqlite2.dbapi2 import OperationalError
import searchengine as se
#bot = se.crawler('') # doesn't work
from bitcrawl import Bot
bot = se.Bot()
try:
    bot.createindextables()
except OperationalError:
    pass
seeds = ['http://kiwitobes.com/wiki/Perl.html']
#seeds = [
#    'http://en.wikipedia.org/wiki/Cognitive_science',
#    'http://en.wikipedia.org/wiki/Working_memory',
#    'http://en.wikipedia.org/wiki/Neuroscience'
#    ]
bot.crawl(seeds)


# for some reason this produces a lot of failed opens (need to use the BitCrawl.Bot class instead of the collective intelligence stuff):
#Indexing http://kiwitobes.com/wiki/Perl.html
#Could not open http://kiwitobes.com/wiki/Module_%28programming%29.html
#Could not open http://kiwitobes.com/wiki/List_%28computing%29.html
#Could not open http://kiwitobes.com/wiki/Free_software.html
#Could not open http://kiwitobes.com/wiki/ANSI.html
#Could not open http://kiwitobes.com/wiki/Perl_%28disambiguation%29.html
#Could not open http://kiwitobes.com/wiki/V6_%28Perl%29.html
#Could not open http://kiwitobes.com/wiki/The_Perl_Foundation.html
#Could not open http://kiwitobes.com/wiki/Subroutine.html
#Could not open http://kiwitobes.com/wiki/Pragma.html
#Could not open http://kiwitobes.com/wiki/O%27Reilly_Media.html
#Could not open http://kiwitobes.com/wiki/Scalar_%28computing%29.html
#Could not open http://kiwitobes.com/wiki/Token_%28parser%29.html
#Could not open http://kiwitobes.com/wiki/Closure_%28computer_science%29.html
#Could not open http://kiwitobes.com/wiki/Perl
#Could not open http://kiwitobes.com/wiki/FreeBSD.html
#Could not open http://kiwitobes.com/wiki/Expression_%28programming%29.html
#Could not open http://kiwitobes.com/wiki/String_%28computer_science%29.html
#Could not open http://kiwitobes.com/wiki/Software_license.html
#Could not open http://kiwitobes.com/wiki/Tar_%28file_format%29.html
#Could not open http://kiwitobes.com/wiki/Sigil_%28computer_programming%29.html
#Could not open http://kiwitobes.com/wiki/Pugs.html
#Could not open http://kiwitobes.com/wiki/Comprehensive_Perl_Archive_Network.html
#Could not open http://kiwitobes.com/wiki/PerlScript.html
#Could not open http://kiwitobes.com/wiki/Gentoo_Linux.html
#Could not open http://kiwitobes.com/wiki/Data_structure.html
#Could not open http://kiwitobes.com/wiki/Unix-like.html
#Could not open http://kiwitobes.com/wiki/Bioinformatics.html
#Could not open http://kiwitobes.com/wiki/Memory_management.html
#Could not open http://kiwitobes.com/wiki/Plain_Old_Documentation.html
#Could not open http://kiwitobes.com/wiki/Mod_perl.html
#Could not open http://kiwitobes.com/wiki/Virtual_machine.html
#Could not open http://kiwitobes.com/wiki/Wikibooks.html
#Could not open http://kiwitobes.com/wiki/Thread_%28computer_science%29.html
#Could not open http://kiwitobes.com/wiki/Code_block.html
#Could not open http://kiwitobes.com/wiki/1987.html
#Could not open http://kiwitobes.com/wiki/S-expression.html
#Could not open http://kiwitobes.com/wiki/BASIC-PLUS.html
#Could not open http://kiwitobes.com/wiki/1994.html
#Could not open http://kiwitobes.com/wiki/Dynamic_language.html
#Could not open http://kiwitobes.com/wiki/Parable_of_the_Pearl.html
#Could not open http://kiwitobes.com/wiki/Newline.html
#Could not open http://kiwitobes.com/wiki/Huffman_coding.html
#Could not open http://kiwitobes.com/wiki/Dynamic_programming_language.html
#Could not open http://kiwitobes.com/wiki/Mac_OS.html
#Could not open http://kiwitobes.com/wiki/AWK_%28programming_language%29.html
#Could not open http://kiwitobes.com/wiki/C_%28programming_language%29.html
#Could not open http://kiwitobes.com/wiki/Evaluation_strategy
#Could not open http://kiwitobes.com/wiki/C%2B%2B.html
#Could not open http://kiwitobes.com/wiki/Mac_OS_X.html
#Could not open http://kiwitobes.com/wiki/LAMP_%28software_bundle%29.html
#Could not open http://kiwitobes.com/wiki/Source_code.html
#Could not open http://kiwitobes.com/wiki/Wiki_software.html
#Could not open http://kiwitobes.com/wiki/Perl_regular_expression_examples.html
#Could not open http://kiwitobes.com/wiki/Perl_Mongers.html
#Could not open http://kiwitobes.com/wiki/Shibboleth
#Could not open http://kiwitobes.com/wiki/Site_Finder.html
#Could not open http://kiwitobes.com/wiki/Latin.html
#Could not open http://kiwitobes.com/wiki/Operating_system.html
#Could not open http://kiwitobes.com/wiki/Randal_L._Schwartz.html
#Could not open http://kiwitobes.com/wiki/1995.html
#Could not open http://kiwitobes.com/wiki/Megabyte.html
#Could not open http://kiwitobes.com/wiki/Perl_DBI.html
#Could not open http://kiwitobes.com/wiki/Regular_expressions.html
#Could not open http://kiwitobes.com/wiki/Constant_folding.html
#Could not open http://kiwitobes.com/wiki/Apache_HTTP_server.html
#Could not open http://kiwitobes.com/wiki/Perl_Object_Environment.html
#Could not open http://kiwitobes.com/wiki/Programming_Perl.html
#Could not open http://kiwitobes.com/wiki/October_26.html
#Could not open http://kiwitobes.com/wiki/Data_compression.html
#Could not open http://kiwitobes.com/wiki/Learning_Perl.html
#Could not open http://kiwitobes.com/wiki/Syntax.html
#Could not open http://kiwitobes.com/wiki/Fortran.html
#Could not open http://kiwitobes.com/wiki/Shell_%28computing%29.html
#Could not open http://kiwitobes.com/wiki/Larry_Wall.html
#Could not open http://kiwitobes.com/wiki/Associative_array.html
#Could not open http://kiwitobes.com/wiki/Just_another_Perl_hacker.html
#Could not open http://kiwitobes.com/wiki/There%27s_more_than_one_way_to_do_it.html
#Could not open http://kiwitobes.com/wiki/Slash_%28weblog_system%29.html
#Could not open http://kiwitobes.com/wiki/Reference_%28computer_science%29.html
#Could not open http://kiwitobes.com/wiki/Perl_interpreter.html
#Could not open http://kiwitobes.com/wiki/December_18.html
#Could not open http://kiwitobes.com/wiki/Benchmark_%28computing%29.html
#Could not open http://kiwitobes.com/wiki/Backtracking.html
#Could not open http://kiwitobes.com/wiki/Shebang_%28Unix%29.html
#Could not open http://kiwitobes.com/wiki/XS_%28Perl%29.html
#Could not open http://kiwitobes.com/wiki/Hello_world.html
#Could not open http://kiwitobes.com/wiki/Pascal_%28programming_language%29.html
#Could not open http://kiwitobes.com/wiki/PCRE.html
#Indexing http://kiwitobes.com/wiki/PCRE.html

 


