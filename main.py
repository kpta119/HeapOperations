from matplotlib import pyplot as plt
from nary_heap import NaryHeap
import random
import time
import gc
import sys


def push_test(heap: NaryHeap):
    time_sections = []
    words_sections = []
    sections_zero = 10000
    currlim = sections_zero
    max = 100000
    while currlim <= max:
        i = 0
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        while i <= currlim:
            heap.push(random.randint(1, 300000))
            i += 1
        stop = time.process_time()
        time_taken = stop - start
        if gc_old:
            gc.enable()
        words_sections.append(currlim)
        time_sections.append(time_taken)
        currlim += sections_zero
    return words_sections, time_sections


def generate_list(n):
    i = 0
    my_list = []
    while i <= n:
        my_list.append(random.randint(1, 300000))
        i += 1
    return my_list


def bulid_test(heap: NaryHeap):
    time_sections = []
    words_sections = []
    sections_zero = 10000
    currlim = sections_zero
    max = 100000
    while currlim <= max:
        my_list = generate_list(currlim)
        heap._table = my_list
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        heap._build_heap()
        stop = time.process_time()
        time_taken = stop - start
        if gc_old:
            gc.enable()
        words_sections.append(currlim)
        time_sections.append(time_taken)
        currlim += sections_zero
    return words_sections, time_sections


def pop_test(heap: NaryHeap):
    time_sections = []
    words_sections = []
    sections_zero = 10000
    currlim = sections_zero
    max = 100000
    while currlim <= max:
        my_list = generate_list(currlim)
        heap._table = my_list
        heap._build_heap()
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        i = 0
        while i <= currlim:
            heap.pop()
            i += 1
        stop = time.process_time()
        time_taken = stop - start
        if gc_old:
            gc.enable()
        words_sections.append(currlim)
        time_sections.append(time_taken)
        currlim += sections_zero
    return words_sections, time_sections


def main(args):
    if __name__ == "__main__":
        binaryHeap = NaryHeap(2)
        fivenaryheap = NaryHeap(5)
        sevenaryheap = NaryHeap(7)
        heaps_names = {
            binaryHeap: "Kopiec Binarny",
            fivenaryheap: "Kopiec 5-arny",
            sevenaryheap: "Kopiec 7-arny"
            }
        for heap in heaps_names.keys():
            words_sections, time_taken = push_test(heap)
            plt.plot(words_sections, time_taken, label=heaps_names.get(heap))
        plt.ylabel('Czas wykonania (sekundy)')
        plt.xlabel('Ilość słów')
        plt.title('Czas pracy kopców (metody push) dla 100000 słów.')
        plt.legend()
        plt.savefig(fname='pushKopców.png')
        plt.show()
        plt.clf()
        for heap in heaps_names.keys():
            words_sections, time_taken = bulid_test(heap)
            plt.plot(words_sections, time_taken, label=heaps_names.get(heap))
        plt.title('Czas pracy kopców (tworzenie) dla list do 100000 elementów')
        plt.ylabel('Czas wykonania (sekundy)')
        plt.xlabel('Ilość słów')
        plt.legend()
        plt.savefig(fname='tworzenieKopców.png')
        plt.show()
        plt.clf()
        for heap in heaps_names.keys():
            words_sections, time_taken = pop_test(heap)
            plt.plot(words_sections, time_taken, label=heaps_names.get(heap))
        plt.title('Czas pracy kopców (metoda pop) 100000 razy')
        plt.ylabel('Czas wykonania (sekundy)')
        plt.xlabel('Ilość operacji')
        plt.legend()
        plt.savefig(fname='popKopców.png')
        plt.show()


main(sys.argv)
