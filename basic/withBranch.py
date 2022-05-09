#!/usr/bin/python3


# with_example01.py
class Sample:
    def __enter__(self):
        print( "In  __enter__()" )
        return "Foo"
    def __exit__(self, type, value, trace):
        print( "In  __exit__()" )

def get_sample():
    return Sample()

with get_sample() as sample:
    print( "sample:", sample )
print(Sample)                                       # 这个表示类本身   <class '__main__.Sample'>
print(Sample())                                     # 这表示创建了一个匿名实例对象 <__main__.Sample object at 0x00000259369CF550>
print( "End of with_example01.py\n")




# with_example02.py
class Sample:
    def __enter__(self):
        return self
    def __exit__(self, type, value, trace):
        print( "type:", type)
        print( "value:", value)
        print( "trace:", trace)
    def do_something(self):
        bar = 1/0
        return bar + 10

with Sample() as sample:
    sample.do_something()
print( "End of with_example02.py\n")