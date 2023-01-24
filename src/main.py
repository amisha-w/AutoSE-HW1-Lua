import sys

from test.NumTest import test_num
from src.utils import coerce,o,oo
import re
from src.the import *

from test import *
from test.SymTest import test_sym
from test.RandTest import RandTest
from test.TheTest import TestThe


def cli(options):
    args = sys.argv[1:]
    for key, value in options.items():
        for n, x in enumerate(args):
            if x == '-'+ key[0] or x == '--'+ key:
                  value = "false" if value == "true" else "true" if value == "false" else args[n+1]
        options[key] = coerce(value)
    return options

def settings(s):
        return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s))


eg = {}
def setEg(the):
    global eg
    eg = {"num": ["check_syms", test_num], "sym": ["check_nums", test_sym], "rand": ["generate, reset, regenerate same", RandTest(the["seed"]).testRand],
          "the" : ["show settings", TestThe(the).testthe]}

def concat(help, testcases):
    help+=help
    for i in testcases:
        help+=" -g  {0}\t{1}\n".format(i, testcases[i][0])
    return help
def main(options, help, funs):
    
    saved = {}
    fails = 0
    for k,v in cli(settings(help)).items():
        options[k] = v
        saved[k] = v
    setEg(options)
    funs = eg
    help = concat(help, eg)

    if options['help']:
        print(help)
    else:
        for what, fun in funs.items():
            if options['go'] == 'all' or options['go'] == what:
                for k,v in saved.items():
                    options[k] = v
                Seed = options['seed']
                if funs[what][1]() == False:
                    fails += 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)
            
if __name__ == '__main__':
    main(the, getConstants('help'),eg)