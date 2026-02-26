# total_salary(path)
# from itertools import count


# with open('salary_file.txt', 'w+') as file:
#     file.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\n')
# def total_salary(path):
#     total = 0
#     count = 0
#     with open(path, 'r', encoding='utf-8') as file:  
#         for line in file:
#             try:
#                 name, salary = line.strip().split(',')
#                 total += int(salary)
#                 count += 1
#             except ValueError:
#                 continue
#     average = total / count if count > 0 else 0
#     return total, average
# total, average = total_salary('salary_file.txt')
# print(f'Total salary: {total}, Average salary: {average}')

# get_cats_info(path)
with open('cats_file.txt', 'w+') as fh:
    fh.write('60b90c1c13067a15887e1ae1,Tayson,3\n\
60b90c2413067a15887e1ae2,Vika,1\n\
60b90c2e13067a15887e1ae3,Barsik,2\n\
60b90c3b13067a15887e1ae4,Simon,12\n\
60b90c4613067a15887e1ae5,Tessi,5\n')
    def get_cats_info(path):
        cats_info = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats_info.append({'id': cat_id, 'name': name, 'age': int(age)})
                except ValueError:
                    continue
        return cats_info
cats = get_cats_info('cats_file.txt')
print(cats)