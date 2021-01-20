print("Hello Python World!")#print会自动换行
import this
\n \t
.lstrip()					#返回去除左空格的值，但不改变原来变量
.rstrip()					#返回去除右空格的值，但不改变原来变量
.title() 					#返回首字母大写的值，但不改变原来变量
.lower() 					#返回全部小写的值，但不改变原来变量
.upper() 					#返回全部大写的值，但不改变原来变量
str(13) --> "13"    		#返回将数字转化为字符串的值，但不改变原来变量
bicycle = ['1', '2']		
square = []					#创立数组，使用中括号
print(bicycle[0])   		#print(bicycle[0].title())
							#数组从0开始索引
							#print(bicycle[-1])返回倒数第一个元素
							#print(bicycle[-2])返回倒数第二个元素等
bicycle[0] = '3'			#替换元素，此时bicycle 为 3 2
bicycle.append('4')			#在末尾添加元素，此时为 3 2 4
bicycle.insert(0, '1')		#在0处添加元素，其余元素右移，此时为 1 3 2 4
del bicycle[1]				#删除1处元素，其余元素左移，此时为 1 2 4
throw = bicycle.pop()		#默认删除最后元素，且将删除元素的值赋给throw
							#此时为 1 2 , throw = 4
throw = bicycle.pop(1)      #删除1处元素，且赋值
							#此时为 1 , throw = 2
bicycle.remove('1')			#查找1在数组中的位置，并删除(但只删除一个)
							#要用循环判断是否全部删除
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()                 #对cars 进行字典序排序
cars.sort(reverse=True)     #对cars 进行字典序反序排序
print(sorted(cars))			#对cars 临时排序并输出
caars.reverse()				#永久颠倒数组元素
							#['subaru', 'toyota', 'audi', 'bmw']
len(cars)					#确定数组长度
for car in cars:
	print(car)				#使用for循环，将cars中的元素存在car中，输出
for car in cars:
	print(car)
	print(car + "!")		#python中的缩进会影响输出，要避免缩进错误
for value in range(1,5):	#输出 1~4, 循环4次, 不输出5
	print(value)
for value in range(5)		#输出 0~4, 循环五次
number = list(range(1,6))	#将数据1~5 存入数组number
number = list(range(2,11,2))#设定步长，将数据 2 4 6 8 10 存入数组number
for value in range(1,11):
	squares.append(value**2)#将 1 4 9···100 存入数组squares
min()
max()
sum()
squares = [value**2 for value in range(1,11)]
							#将 1 4 9···100 存入数组squares
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])			#输出从0到3处的元素
print(players[1:])			#输出从1以后的元素
print(players[:3])			#输出从3以前的元素
print(players[:])			#输出全部元素
print(players[-3:])			#输出最后三个元素

for player in players[:3]:	#输出3以前的元素
	print(player.title()) 
players_ = players[:] 		#将players的元素复制到players_
#注意： friend_foods = my_foods 这样不行！这样使得两个数组指向同一个列表，导致两者的变化同步
dimensions = (200 , 50)		#使用圆括号定义元组, 其中0处元素为200, 1处元素为50
#dimensions[0] = 250 ×错误	#元组中的元素不能改变
dimensions = (400 , 100)	#但是再次给元组赋值是合法的

if a==b :
	print ···
if a!=b :
	print ···
if a == 1 and b == 1 ···
if a == 1 or b == 1 ···

if 'charles' in players ···
if 'charles' not in players ···

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:						#此处的 else 也可以用 elif 代替
	price = 10				#if - elif - else 格式
food = [] 
if food:					#若food 不为空，则执行；若为空, 则返回false
	for ···

alien_0 = {'color': 'green', 'points': 5}
							#使用大括号定义字典
print(alien_0['color'])		#使用字典储存数据的不同属性：color与points
print(alien_0['points']) 	#'color':'green' 构成键-值对
alien_0['x_position'] = 0	#向字典中添加键-值对
alien_0['y_position'] = 25 
#{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
#这个字典的最终版本包含四个键—值对，注意，键—值对的排列顺序与添加顺序不同。
#Python不关心键—值对的添加顺序，而只关心键和值之间的关联关系。
alien_0['num'] = 11			#向字典中添加'num' : 11 的键值对
alien_0 = {'color': 'green'}
alien_0['color'] = 'yellow'	#修改字典中的元素
del alien_0['num']			#删除字典中num对应的键值对
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}  						#使用特殊缩进格式使得字典内容更加清晰
for key, value in user_0.items():
							#当从字典中调用 键与值 时，要使用.items()函数
	print("\nKey: " + key)	#在for中声明两个变量，用于输出键-值对
	print("Value: " + value)#但输出结果未必按顺序，python只关心键-值对的对应关系

for name in favorite_languages.keys():
	print(name.title())		#.key()函数可以只提取字典中的'键'
if 'erin' not in favorite_languages.keys():
							#用于确定某元素是否在字典的'键'中
for name in sorted(favorite_languages.keys())
	print(name)				#将字典中元素按照键的字典序暂时排序后输出键

for value in favorite_languages.values():
	print(value.title())	#.value()函数可以只提取字典中的'值', 但这样可能会有重复的数据
for value in set(favorite_languages.values()):
	print(value.title())	#使用set()函数进行去重，使得'值'构成无重复元素的集合
if 'erin' not in favorite_languages.values():
							#用于确定某元素是否在字典的'值'中
aliens = []					#使用中括号创建字典的列表，用于将字典集合起来
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)#使用.append()将new_alien字典添加到aliens列表中

print(len(aliens))			#使用len()输出aliens包含的字典个数
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}						#使用中括号创建列表，此时是将列表嵌套在字典中
for topping in pizza['toppings']:
	print(topping+"\n")		#输出字典中的列表
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	} 						#字典中的列表
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
		for language in languages:
		print("\t" + language.title())
							#使用嵌套for输出字典
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}						#字典的嵌套
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
message = input("Tell me something")
print(message)				#在屏幕显示内容，并将输入存在message变量中

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? " 
							#使用+=符号，实现存储换行的字符串
age = input("How old are you? ")
age = int(age)				#使用int()函数，将输入的字符型数据转为整型数据，才能使用逻辑运算等，如 >=, != 等

number = 1
while number <= 5:
	print(number)
	number += 1				#输出1~5

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)		#设计标记active，判断是否退出

while True:
	city = input(prompt)

	if city == 'quit':
		break 
	else:
		print(city.title())	#使用while True 使其死循环，再用break 退出

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number) 	#continue使程序忽略后续，回到循环开始处

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
	pets.remove('cat')		#使用while删除列表中的全部'cat'元素
	
"""在一个范围内显示注释"""

def greet():
	print ("Hello!")		#定义函数(要有冒号)
	
def greet_user(username):	#向函数传递变量
	print(username.title())	#username是形式变量
							#形式变量与实际变量的名字可以相同，且修改形式变量不会改变实际变量的值
def describe_pet(animal_type, pet_name):
	print(animal_type)
	print(pet_name)
"""
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
由于使用了关键字实参指定了形参名， 二者的调用输出结果相同
"""
def describe_pet(name, type_='dog'):
"""为type_变量设定默认值""" 
describe_pet(name='willie')
"""
使得调用函数时只要指定name的值，但由于默认调用第一个形参，所以要在函数中
把name放在type_的前面
describe_pet(name='harry', type='hamster')
describe_pet('harry','hamster')
二者的结果相同
若为函数提供了实参，则函数会忽略形参的默认值
"""
def full_name(first_name, last_name):
	full = first_name + ' ' + last_name
	return full.title()		#返回值为全名
def build_person(first_name, last_name):
	person = {'first': first_name, 'last': last_name}
	return person			#返回一个字典，其中包含有关一个人的信息

def greet_users(names):
	for name in names:
	msg = "Hello, " + name.title() + "!"
	print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)		#向函数传递一个列表，并对于列表中每一个元素都进行回应

def print_models(unprinted, completed):
	while unprinted:
		current_design = unprinted.pop()
							#模拟根据设计制作3D打印模型的过程
		print("Printing model: " + current_design)
		completed.append(current_design)
unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
completed = []
print_models(unprinted, completed) 
							#调用函数时，列表被传递给函数，此时对列表的修改会导致列表改变
							#这与形参和实参的结果不同
"""若想要不修改列表的值，则应该向函数传递一个切片的副本"""
print_models(unprinted[:], completed)
							#执行函数后会发现unprinted和completed的列表内容是一样的
"""
注意python的列表不同于c的数组，其大小是不固定的，
因此添加元素的时候要使用append，不能盲目使用  xxx[i]=···  有的时候会导致数组越界
"""

def make_pizza(*toppings):
	print(toppings)			#使用任意数量的关键字实参，用*创建列表
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
							#在形参前加上*使得函数可以接受任意数量的实参
							#函数实际上创建了一个toppings的元组
def build_profile(first, last, **user_info):
	profile = {}			#使用两个**来创建字典
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile			#使用任意数量的关键字实参，向字典中添加键值对

user = build_profile('wu', 'jing hao',food='dabian',hobby='eat_shit')
							#向字典中添加键值对时，food = 'dabian'
							#前面的"键"不需要加引号，而"值"需要加引号
"""在代码中导入模块："""
"""在目录下创建pizza.py，其中包含函数："""
def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) +
	for topping in toppings:
	print("- " + topping) 
"""在同目录下创建make_pizza.py，在这个程序中，我们要导入make_pizza()函数"""
import pizza				#使用import 指令打开pizza.py文件，从而导入函数
							#接下来就可以调用pizza.py中的make_pizza()函数
pizza.make_pizza(16, 'pepperoni')
							#由于未指名导入了pizza.py中的哪些函数
							#在调用函数时要使用句点，指名函数出处
"""也可以从文件中导入特定函数"""
"""
若使用这种语法，调用函数时就无需使用句点。
由于我们在import语句中显式地导入了函数make_pizza()
因此调用它时只需指定其名称
"""
from pizza import make_pizza#此代码可以从pizz.py中导入make_pizza()函数
from module_name import function_0, function_1, function_2
							#用逗号分隔函数名，则可导入多个函数
make_pizza(16, 'pepperoni') #无需句点的调用函数
"""可以用as语句为别的文件中导入的函数指定别名"""
from pizza import make_pizza as mp
							#将从pizza.py导入的make_pizza()函数指名为mp()
mp(16, 'pepperoni')			#使用别名调用函数

from pizza import *			#使用*可以直接导入pizza.py中的全部函数

make_pizza(16, 'pepperoni')	#进而在调用函数时也可以不使用句点
"""
然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法：
如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：
Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。
"""
"""
函数编写指南
1、应给函数指定描述性名称，且只在其中使用小写字母和下划线
2、每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面
3、给形参指定默认值时，等号两边不要有空格：
def function_name(parameter_0, parameter_1='default value')
   对于函数调用中的关键字实参，也应遵循这种约定：
function_name(value_0, parameter_1='value') 
"""
class Dog():				#创建一个Dog的类，其中类的首字母一般大写
"""类中的函数称为方法，_init_()为特殊方法，且必然包含形参self"""
	def __init__(self, name, age):
		self.name = name
		self.age = age			#初始化属性name和age
"""
只需要为形参中的name和age提供值
以self为前缀的变量都可供类中的所有方法使用
我们还可以通过类的任何实例来访问这些变量
像这样可通过实例访问的变量称为属性
"""
	def sit(self):
		print(self.name.title() + " is now sitting.")
	def roll_over(self):
		print(self.name.title() + " rolled over!") 
"""
这两个函数只有一个形参self，通过句点调用变量
"""
my_dog = Dog('willie', 6)	#调用Dog 类
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)	#创建多个实例

class Car():

	def __init__(self, make, model, year):
	self.make = make
	self.model = model
	self.year = year
	self.odometer_reading = 0
							#创建一个属性，并为该属性指定默认值

my_new_car = Car('audi', 'a4', 2016)
							#调用类
my_new_car.odometer_reading = 23
							#修改属性的值
class Car():
	==snip==				#在类中创建函数，并引入形参
	def update_odometer(self, mileage):
							#引入参数都要创建self变量
		self.odometer_reading = mileage
"""通过方法修改属性的值"""
	def increment_odometer(self, miles):
							#如此修改能够实现递增
		self.odometer_reading += miles
							#通过if使得增量无法为负值
"""一以下代码可以实现类的继承"""
class Car():
	def __init__(self, make, model, year):
	···
class Electricar(Car):
"""定义子类时，必须在括号内指定父类的名称,且父类一定要在子类之前定义"""
	def __init__(self, make, model, year):
	super().__init__(make, model, year)
"""
super()是一个特殊函数，帮助Python将父类和子类关联起来。
这行代码让Python调用ElectricCar的父类的方法__init__()，
让ElectricCar实例包含父类的所有属性。父类也称为超类（superclass）
名称super因此而得名。
"""
class ElectricCar(Car):		
	def __init__(self, make, model, year):
	super().__init__(make, model, year)
	self.battery_size = 70	#此代码可以给ElectricCar添加新的属性，而不会改变Car的属性

class Car():				#以下代码可以重写父类
	def fill_gas_tank():
	···
"""
假设Car类有一个名为fill_gas_tank()的方法，
它对全电动汽车来说毫无意义，因此你可能想重写它
"""
class ElectricCar(Car):
	def fill_gas_tank():
		print(···)
"""
如果有人对ElectricCar调用方法fill_gas_tank()，
Python将忽略Car类中的方法fill_gas_tank()，转而运行上述代码。
使用继承时，可让子类保留从父类那里继承而来的精华，并剔除不需要的糟粕。
"""
class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
	def describe(self):
		···
class ElectricCar(Car):
	def __init__(self, make, model, year):
	super().__init__(make, model, year)
	self.battery = Battery()#将Battery中的函数(包括describe)套在self.battery中
"""
让Python创建一个新的Battery实例（由于没有指定尺寸，因此为默认值70）
并将该实例存储在属性self.battery中
"""
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
#从而可以使用多点嵌套
#创建一个car.py的文件，其中只包含Car的类
from car import Car			#从car.py文件导入Car类
from car import Car, ElectricCar
							#从car.py文件导入多个类
import car 					#导入整个模块
from car import *			#导入car.py模块的所有类
"""
不推荐使用这种导入方式，其原因有二。
首先，如果只要看一下文件开头的import语句，就能清楚地知道程序使用了哪些类，
将大有裨益；但这种导入方式没有明确地指出你使用了模块中的哪些类。
这种导入方式还可能引发名称方面的困惑。如果你不小心导入了一个与程序文件中其
他东西同名的类，将引发难以诊断的错误。
"""
from collections import OrderedDict
							#导入python标准库，使得按顺序添加键值对
"""
创建文件
pi_digits.txt
3.1415926535
  8979323846
  2643383279
"""
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())#读取文件并输出,同时删除行尾的空白

file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object: 
							#使用绝对路径读取文件(as file_object)

filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())#去除行尾回车

filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())	#创建一个包含文件各行内容的列表
"""
readlines()从文件中读取每一行，并将其存储在一个列表中；
接下来，该列表被存储到变量lines中；
在with代码块外，我们依然可以使用这个变量。
"""
pi_string = ''
for line in lines:
	pi_string += line.strip()
							#删除左右空格
print(pi_string)
print(len(pi_string))		#将文件中的列表储存在pi_string中，并输出其长度

birthday = input("Enter your birthday")
if birthday in pi_string:
	print("Yes!")
else:
	print("No!")			#判断一段文字是否在文件中

message = "I really like dogs."
message.replace('dog', 'cat')
"""将文本中的dog替换为cat，输出 I really like cats."""

filename = 'programming.txt'
with open(filename, 'w') as file_object:
	file_object.write("I love programming.")
"""
在这个示例中，调用open()时提供了两个实参。
第一个实参也是要打开的文件的名称；
第二个实参（'w'）告诉Python，我们要以写入模式打开这个文件。
打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）
或让你能够读取和写入文件的模式（'r+'）。
如果你省略了模式实参，Python将以默认的只读模式打开文件。
"""
#函数write()不会在你写入的文本末尾添加换行符，
#因此如果你写入多行时没有指定换行符，文件看起来可能不是你希望的那样：
#要让每个字符串都单独占一行，需要在write()语句中包含换行符 \n:
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")
"""
如果你要给文件添加内容，而不是覆盖原有的内容，可以附加模式打开文件。
你以附加模式打开文件时，Python不会在返回文件对象前清空文件，
而你写入到文件的行都将添加到文件末尾。
如果指定的文件不存在，Python将为你创建一个空文件。
"""
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

try:
	print(5/0)				#使用try-except代码块
except ZeroDivisionError:
	print("You can't divide by zero!")
"""
我们将导致错误的代码行print(5/0)放在了一个try代码块中。
如果try代码块中的代码运行起来没有问题，Python将跳过except代码块；
如果try代码块中的代码导致了错误，Python将查找这样的except代码块，
并运行其中的代码，即其中指定的错误与引发的错误相同。
"""
try:
	answer = int(first_number) / int(second_number)
except ZeroDivisionError:
	print("You can't divide by 0!")
else:
	print(answer)			#使用else代码块，避免显示崩溃数据
"""
方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点
"""
words = contents.split()
num_words = len(words)
print(num_words)			#计算文件大致包含几个单词
ctrl + /                    #集体注释