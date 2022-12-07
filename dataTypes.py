#Some built-in data types of Python
'''
      1. Numeric data: int, float, complex
            int: 3, -8, 0
            float: 7.349
            complex: 6+2i

      2. text data: string (str)
            str:"Hello World"

      3. Boolean data
            true, false, 0, 1

      4. Sequenced data: list, tuple
            list: ordered collection of data with elements separated by a comma and enclosed within square brackets. Liss are mutable and can be modified after creation.

            tuple: ordered collection of data with elements separaed by a comma and enclosed within parantheses. Tuples are immutable and cannot be modified after creation.

      5. Mapped data: dict
            dict: unordered collection of data containing a key:value pair.
'''


a=complex(8, 2)   #equivalent to 8+2j
print(a)

list1=[8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1=(("parrot", "sparrow"), ("lion", "tiger"))
print(tuple1)


dict1={"name":"Bipin", "age":20, "canVote":True}
print(dict1)