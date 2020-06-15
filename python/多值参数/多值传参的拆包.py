def demo(*args, **kwargs):
    print(args)

    print(kwargs)


nums = (1, 2, 3)
GHY = {"name": "郭浩远", "age": 24}

# 拆包可以简化多值传递
demo(*nums, **GHY)

demo(1, 2, 3, name="郭浩远", age=24)