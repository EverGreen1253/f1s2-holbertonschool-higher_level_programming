#!/usr/bin/python3
pick = __import__('task_01_pickle')

def main():
    """ main function """

    # Create an instance of CustomObject
    obj = pick.CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = pick.CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()

if __name__ == "__main__":
    main()
