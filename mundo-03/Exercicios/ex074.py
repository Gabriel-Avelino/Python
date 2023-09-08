from random import randint
nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end='')
for pos, n in enumerate(nums):
    print(nums[pos], end=' ')

print(f'\nO maior valor sorteado foi {max(nums)}')
print(f'O menor valor sorteado foi {min(nums)}')
