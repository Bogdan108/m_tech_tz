
class Pyramid:
    def __init__(self, pyramid):
        self.pyramid_str = pyramid

    # Преобразуем исходную строку в большую пирамиду в виде списка
    def pyramid_transform(self, pyramid_str: str, flag: bool):
        #флаг означает переворачиваем ли мы строку для удобства построения пирамиды
        length = len(pyramid_str)
        if flag:
            reversed_string = pyramid_str
        else:
            reversed_string = pyramid_str[::-1]
        pyramid_list = []
        lower, upper = 0, 1
        while upper < length+1:
            pyramid_list.append(reversed_string[lower:upper])
            temp = upper
            upper = 2*upper-lower+2
            lower = temp
        return pyramid_list

    # Преобразуем большую пирамиду в список маленьких треугольников по 4 элемента
    def triangle_transform(self, pyramid_list: list):
        # False - upper, True - down данный флаг обозначает на какой строке расположена верхушка треугольника
        axis = False
        triangle_list = []

        for i in range(0, len(pyramid_list), 2):
            j = 0
            axis = False
            while j < len(pyramid_list[i]):
                new_str = ''
                if axis == False:
                    new_str += pyramid_list[i][j]
                    new_str += pyramid_list[i+1][j:j+3]
                    j += 1
                else:
                    new_str += pyramid_list[i][j:j+3]
                    new_str += pyramid_list[i+1][j+2]
                    j += 3
                axis = not axis
                triangle_list.append(new_str)
        return triangle_list

    # Проверяем возможно ли сжать треугольник
    def is_compressed_triangles(self, triangle_list: list):
        can_transform = True
        for i in triangle_list:
            if len(set(list(i))) != 1:
                can_transform = False
        return can_transform

    # Обработка основоного алгоритма сжатия
    def compress_triangles(self, inverse=False):
        if len(self.pyramid_str) > 1:
            pyramid_list = self.pyramid_transform(self.pyramid_str, inverse)
            triangle_list = self.triangle_transform(pyramid_list,)

            if self.is_compressed_triangles(triangle_list):
                # Сжатие текущей строки и получение новой
                new_pyramid_str = ''
                for i in triangle_list:
                    new_pyramid_str += i[0]
                self.pyramid_str = new_pyramid_str
                return self.compress_triangles(True)
            else:
                answer_str = ""
                for i in pyramid_list:
                    answer_str += i
                return answer_str[::-1]
        else:
           return self.pyramid_str

# input.txt
# input1.txt
# input2.txt
# input3.txt
with open('input/input1.txt', 'r') as input:
    file_content = input.read()

pyramid_string = file_content
pyramid = Pyramid(pyramid_string)
answer = pyramid.compress_triangles()

with open("output.txt", "w") as output:
    output.write(answer)
