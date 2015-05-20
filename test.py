import timeit
import time
from threading import Timer
import random
from string import maketrans
from Bio.Seq import Seq

# --------------------------------------
# reverse complement sequence:
# --------------------------------------


def reversecomplement():
    '''Reverse complement'''
    comp = ''
    for s in seq:
        if s == 'A':
            comp = comp + 'T'
        elif s == 'T':
            comp = comp + 'A'
        elif s == 'C':
            comp = comp + 'G'
        elif s == 'G':
            comp = comp + 'C'
        else:
            comp = comp + s
    return comp[::-1]


def reversecomplement_faster_A():
    '''Reverse complement'''
    mapping = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join([mapping.get(s, s) for s in seq])[::-1]


def reversecomplement_faster_A1():
    '''Reverse complement'''
    mapping = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join(mapping.get(s, s) for s in seq)[::-1]


def reversecomplement_faster_B():
    '''Reverse complement'''
    mapping = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join([mapping.get(s, s) for s in reversed(seq)])


def reversecomplement_faster_B1():
    '''Reverse complement'''
    mapping = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join(mapping.get(s, s) for s in reversed(seq))


def reversecomplement_faster_C():
    '''Reverse complement'''
    reverse = []
    mapping = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    for s in seq:
        reverse.append(mapping.get(s, s))
    return ''.join(reverse)[::-1]


def ReverseComplementSUPERFAST():
    return seq.translate(maketrans("ATGC", "TACG"))[::-1]


def ReverseComplementBIOPython():
    my_seq.reverse_complement()


if __name__ == '__main__':
    import timeit
    # Global to make it visible to all functions
    seq = ''.join(random.choice('CGTA') for _ in xrange(10000))
    print 'Old and slow string concat'
    print (timeit.timeit(
        """reversecomplement()""",
        number=1000,
        setup="from __main__ import reversecomplement"))

    print "''.join([mapping.get(s, s) for s in seq])[::-1]"
    print (timeit.timeit(
        """reversecomplement_faster_A()""",
        number=1000,
        setup="from __main__ import reversecomplement_faster_A"))

    print "''.join(mapping.get(s, s) for s in seq)[::-1]"
    print (timeit.timeit(
        """reversecomplement_faster_A1()""",
        number=1000,
        setup="from __main__ import reversecomplement_faster_A1"))

    print "''.join([mapping.get(s, s) for s in reversed(seq)])"
    print (timeit.timeit(
        """reversecomplement_faster_B()""",
        number=1000,
        setup="from __main__ import reversecomplement_faster_B"))

    print "''.join(mapping.get(s, s) for s in reversed(seq))"
    print (timeit.timeit(
        """reversecomplement_faster_B1()""",
        number=1000,
        setup="from __main__ import reversecomplement_faster_B1"))

    print """
    for s in seq:
        reverse.append(mapping.get(s, s))
    return ''.join(reverse)[::-1] """
    print (timeit.timeit(
        """reversecomplement_faster_C()""",
        number=1000,
        setup="from __main__ import reversecomplement_faster_C"))

    print 'seq.translate(maketrans("ATGC","TACG"))[::-1]'
    print (timeit.timeit(
        """ReverseComplementSUPERFAST()""",
        number=1000,
        setup="from __main__ import ReverseComplementSUPERFAST"))
    print 'Reverse Bio PYthon'
    my_seq = Seq(seq)
    print (timeit.timeit(
        """ReverseComplementBIOPython()""",
        number=1000,
        setup="from __main__ import ReverseComplementBIOPython"))
