# ========================================
# أساسيات Python - دورة الأمن السيبراني
#  Group_A - المرحلة الثانية
# ========================================

print("مرحباً بكم في دورة أساسيات Python! 🐍")
print("=" * 50)

# ========================================
# 1. المتغيرات وأنواع البيانات (Variables & Data Types)
# ========================================

print("\n📚 الدرس الأول: المتغيرات وأنواع البيانات")
print("-" * 40)

# الأرقام الصحيحة (Integers)
age = 20
student_id = 2024001
print(f"العمر: {age}")
print(f"رقم الطالب: {student_id}")
print(f"نوع البيانات: {type(age)}")

# الأرقام العشرية (Floats)
gpa = 3.75
temperature = 25.5
print(f"المعدل: {gpa}")
print(f"درجة الحرارة: {temperature}")
print(f"نوع البيانات: {type(gpa)}")

# النصوص (Strings)
student_name = "أحمد محمد"
course_name = "أساسيات البرمجة"
print(f"اسم الطالب: {student_name}")
print(f"اسم المادة: {course_name}")
print(f"نوع البيانات: {type(student_name)}")

# القيم المنطقية (Booleans)
is_enrolled = True
is_graduated = False
print(f"مسجل في المادة: {is_enrolled}")
print(f"تخرج: {is_graduated}")
print(f"نوع البيانات: {type(is_enrolled)}")

# ========================================
# 2. العمليات الحسابية (Arithmetic Operations)
# ========================================

print("\n🧮 الدرس الثاني: العمليات الحسابية")
print("-" * 40)

num1 = 15
num2 = 7

print(f"الرقم الأول: {num1}")
print(f"الرقم الثاني: {num2}")
print(f"الجمع: {num1} + {num2} = {num1 + num2}")
print(f"الطرح: {num1} - {num2} = {num1 - num2}")
print(f"الضرب: {num1} * {num2} = {num1 * num2}")
print(f"القسمة: {num1} / {num2} = {num1 / num2}")
print(f"القسمة الصحيحة: {num1} // {num2} = {num1 // num2}")
print(f"باقي القسمة: {num1} % {num2} = {num1 % num2}")
print(f"الأس: {num1} ** 2 = {num1 ** 2}")

# ========================================
# 3. أخذ المدخلات من المستخدم (User Input)
# ========================================

print("\n⌨️ الدرس الثالث: أخذ المدخلات من المستخدم")
print("-" * 40)

# مثال بسيط
print("مثال: إدخال بيانات الطالب")
name = input("أدخل اسمك: ")
age = int(input("أدخل عمرك: "))
print(f"مرحباً {name}، عمرك {age} سنة")

# مثال على العمليات الحسابية
print("\nمثال: حاسبة بسيطة")
num1 = float(input("أدخل الرقم الأول: "))
num2 = float(input("أدخل الرقم الثاني: "))
result = num1 + num2
print(f"النتيجة: {num1} + {num2} = {result}")

# ========================================
# 4. الجمل الشرطية (Conditional Statements)
# ========================================

print("\n🔍 الدرس الرابع: الجمل الشرطية")
print("-" * 40)

# مثال 1: فحص العمر
age = int(input("أدخل عمرك: "))

if age >= 18:
    print("أنت بالغ")
else:
    print("أنت قاصر")

# مثال 2: تقييم الدرجة
grade = int(input("أدخل درجتك (0-100): "))

if grade >= 90:
    print("ممتاز!")
elif grade >= 80:
    print("جيد جداً")
elif grade >= 70:
    print("جيد")
elif grade >= 60:
    print("مقبول")
else:
    print("راسب")

# مثال 3: فحص كلمة المرور
password = input("أدخل كلمة المرور: ")

if len(password) >= 8:
    print("كلمة المرور قوية")
else:
    print("كلمة المرور قصيرة")

# مثال 4: فحص الرقم الزوجي أو الفردي
number = int(input("أدخل رقماً: "))

if number % 2 == 0:
    print("الرقم زوجي")
else:
    print("الرقم فردي")

# ========================================
# 5. الحلقات التكرارية (Loops)
# ========================================

print("\n🔄 الدرس الخامس: الحلقات التكرارية")
print("-" * 40)

# مثال 1: طباعة الأرقام من 1 إلى 5
print("الأرقام من 1 إلى 5:")
for i in range(1, 6):
    print(i)

# مثال 2: طباعة أسماء الطلاب
students = ["أحمد", "فاطمة", "محمد", "سارة", "علي"]
print("\nأسماء الطلاب:")
for student in students:
    print(f"- {student}")

# مثال 3: حساب مجموع الأرقام
numbers = [1, 2, 3, 4, 5]
total = 0
print(f"\nحساب مجموع الأرقام: {numbers}")

for num in numbers:
    total += num
    print(f"أضف {num}، المجموع الآن: {total}")

print(f"المجموع النهائي: {total}")

# مثال 4: عد الأرقام الزوجية
print("\nالأرقام الزوجية من 1 إلى 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# مثال 5: جدول الضرب
print("\nجدول ضرب الرقم 5:")
for i in range(1, 11):
    result = 5 * i
    print(f"5 × {i} = {result}")

# ========================================
# 6. القوائم (Lists)
# ========================================

print("\n📋 الدرس السادس: القوائم (Lists)")
print("-" * 40)

# إنشاء قائمة
fruits = ["تفاح", "موز", "برتقال", "فراولة"]
print(f"الفواكه: {fruits}")

# الوصول للعناصر
print(f"أول فاكهة: {fruits[0]}")
print(f"آخر فاكهة: {fruits[-1]}")
print(f"الفواكه من 1 إلى 3: {fruits[1:4]}")

# إضافة عنصر
fruits.append("عنب")
print(f"بعد إضافة العنب: {fruits}")

# إدراج عنصر في موضع محدد
fruits.insert(2, "ليمون")
print(f"بعد إدراج الليمون: {fruits}")

# حذف عنصر
fruits.remove("موز")
print(f"بعد حذف الموز: {fruits}")

# طول القائمة
print(f"عدد الفواكه: {len(fruits)}")

# فحص وجود عنصر
if "تفاح" in fruits:
    print("التفاح موجود في القائمة")
else:
    print("التفاح غير موجود")

# مثال تطبيقي: قائمة التسوق
shopping_list = ["خبز", "حليب", "بيض", "جبن"]
print(f"\nقائمة التسوق: {shopping_list}")

# إضافة عنصر جديد
new_item = input("أضف عنصراً جديداً: ")
shopping_list.append(new_item)
print(f"قائمة التسوق المحدثة: {shopping_list}")

# فحص العناصر المشتراة
bought_item = input("أدخل العنصر الذي اشتريته: ")
if bought_item in shopping_list:
    shopping_list.remove(bought_item)
    print(f"تم حذف {bought_item} من القائمة")
    print(f"القائمة المتبقية: {shopping_list}")
else:
    print(f"{bought_item} غير موجود في القائمة")

# ========================================
# 7. القواميس (Dictionaries)
# ========================================

print("\n📚 الدرس السابع: القواميس (Dictionaries)")
print("-" * 40)

# إنشاء قاموس بسيط
student = {
    "name": "أحمد محمد",
    "age": 20,
    "grade": 85,
    "major": "علوم الحاسب"
}

print("معلومات الطالب:")
print(f"الاسم: {student['name']}")
print(f"العمر: {student['age']}")
print(f"الدرجة: {student['grade']}")
print(f"التخصص: {student['major']}")

# إضافة معلومات جديدة
student["email"] = "ahmed@example.com"
student["phone"] = "0501234567"

print(f"\nبعد إضافة معلومات جديدة:")
print(f"البريد الإلكتروني: {student['email']}")
print(f"رقم الهاتف: {student['phone']}")

# عرض جميع المعلومات
print(f"\nجميع المعلومات:")
for key, value in student.items():
    print(f"{key}: {value}")

# مثال تطبيقي: قاموس درجات الطلاب
grades = {
    "أحمد": 85,
    "فاطمة": 92,
    "محمد": 78,
    "سارة": 96,
    "علي": 88
}

print(f"\nدرجات الطلاب:")
for student_name, grade in grades.items():
    print(f"{student_name}: {grade}")

# البحث عن طالب
search_name = input("\nأدخل اسم الطالب للبحث عن درجته: ")
if search_name in grades:
    print(f"درجة {search_name}: {grades[search_name]}")
else:
    print(f"{search_name} غير موجود")

# حساب متوسط الدرجات
total_grades = sum(grades.values())
average = total_grades / len(grades)
print(f"\nمتوسط الدرجات: {average:.2f}")

# العثور على أعلى وأقل درجة
highest_grade = max(grades.values())
lowest_grade = min(grades.values())

print(f"أعلى درجة: {highest_grade}")
print(f"أقل درجة: {lowest_grade}")

# مثال آخر: قاموس معلومات المنتجات
products = {
    "لابتوب": {
        "price": 3000,
        "brand": "Dell",
        "in_stock": True
    },
    "هاتف": {
        "price": 1500,
        "brand": "Samsung",
        "in_stock": False
    },
    "سماعات": {
        "price": 200,
        "brand": "Sony",
        "in_stock": True
    }
}

print(f"\nمعلومات المنتجات:")
for product, details in products.items():
    print(f"\n{product}:")
    print(f"  السعر: {details['price']} دينار")
    print(f"  الماركة: {details['brand']}")
    print(f"  متوفر: {'نعم' if details['in_stock'] else 'لا'}")

# ========================================
# ملخص الدرس
# ========================================

print("\n" + "=" * 50)
print("🎯 ملخص ما تعلمناه اليوم:")
print("=" * 50)
print("1. ✅ المتغيرات وأنواع البيانات")
print("2. ✅ العمليات الحسابية")
print("3. ✅ أخذ المدخلات من المستخدم")
print("4. ✅ الجمل الشرطية")
print("5. ✅ الحلقات التكرارية")
print("6. ✅ القوائم وعملياتها")
print("7. ✅ القواميس واستخداماتها")
print("\n🐍 تهانينا! لقد أتممت أساسيات Python!")
print("=" * 50)