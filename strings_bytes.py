# strings and bytes are not interchangeable
# strings contain unicode, bytes are raw 8 bit values


def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string."
    print(s)

    # TODO: Try combiningh them
    # print(s+b) Throws a string concatenation error

    # TODO: Bytes and strings need to be properly encoded and decoded
    # before you can work on them together.
    s2 = b.decode('utf-8')
    print(s+s2)
    b2 = s.encode('utf-8')
    print(b+b2)

    # TODO: encode the string as UTF-32
    b3 = s.encode('utf-32')
    print(b+b3)

    # TODO: try changing encoding to UTF-32
    s3 = b.decode('utf-8')
    b4 = s3.encode('utf-32')
    print(b3+b4)


if __name__ == '__main__':
    main()
