class MemoryFriendlyCorpus(object):
    def __iter__(self):
        for line in open("mytoycorpus.txt"):
            yield line


