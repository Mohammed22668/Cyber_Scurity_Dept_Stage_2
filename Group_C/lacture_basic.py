# # ========================================
# # أساسيات Python - دورة الأمن السيبراني
# # المجموعة الثالثة - المرحلة الثانية
# # ========================================

# print("مرحباً بكم في دورة أساسيات Python! 🐍")
# print("=" * 50)

# # ========================================
# # 1. أساسيات البرمجة وأنواع البيانات
# # ========================================

# print("\n📚 الدرس الأول: أساسيات البرمجة وأنواع البيانات")
# print("-" * 50)

# # أنواع البيانات الأساسية مع أمثلة عملية
# system_id = 1001
# temperature = 25.5
# device_name = "Laptop_Office"
# is_working = True

# print(f"معرف النظام: {system_id} (نوع: {type(system_id)})")
# print(f"درجة الحرارة: {temperature}°C (نوع: {type(temperature)})")
# print(f"اسم الجهاز: {device_name} (نوع: {type(device_name)})")
# print(f"الجهاز يعمل: {is_working} (نوع: {type(is_working)})")

# # العمليات على النصوص
# print("\n📝 العمليات على النصوص:")
# message = "Welcome to Python Programming Course"
# print(f"الرسالة: {message}")
# print(f"طول الرسالة: {len(message)} حرف")
# print(f"الرسالة تبدأ بـ Welcome: {'Welcome' in message}")
# print(f"الرسالة بالأحرف الكبيرة: {message.upper()}")
# print(f"عدد كلمة 'to': {message.count('to')}")

# # تحويل الأنواع
# print("\n🔄 تحويل أنواع البيانات:")
# date_str = "2024-01-15"
# number_str = "100"
# print(f"التاريخ كنص: {date_str} (نوع: {type(date_str)})")

# # تحويل الأرقام
# score_str = "85.5"
# count_str = "50"
# score_float = float(score_str)
# count_int = int(count_str)

# print(f"الدرجة: {score_float} (نوع: {type(score_float)})")
# print(f"العدد: {count_int} (نوع: {type(count_int)})")

# # ========================================
# # 2. العمليات الحسابية والمنطقية المتقدمة
# # ========================================

# print("\n🧮 الدرس الثاني: العمليات الحسابية والمنطقية المتقدمة")
# print("-" * 50)

# # حسابات بسيطة
# total_students = 100
# passed_students = 85
# failed_students = total_students - passed_students
# pass_rate = (passed_students / total_students) * 100

# print(f"إجمالي الطلاب: {total_students}")
# print(f"الطلاب الناجحون: {passed_students}")
# print(f"الطلاب الراسبون: {failed_students}")
# print(f"نسبة النجاح: {pass_rate}%")

# # تحليل الأداء
# if pass_rate >= 90:
#     print("🎉 أداء ممتاز!")
# elif pass_rate >= 80:
#     print("👏 أداء جيد جداً")
# elif pass_rate >= 70:
#     print("👍 أداء جيد")
# elif pass_rate >= 60:
#     print("📈 أداء مقبول")
# else:
#     print("📚 يحتاج تحسين")

# # العمليات المنطقية المعقدة
# print("\n🔗 العمليات المنطقية المعقدة:")
# has_internet = True
# has_computer = True
# has_time = False
# is_motivated = True

# # منطق التعلم
# can_study = (has_internet and has_computer) or (has_time and is_motivated)
# print(f"يمكن الدراسة: {can_study}")

# # تحليل متعدد الشروط
# study_conditions = [
#     ("اتصال الإنترنت", has_internet),
#     ("جهاز حاسوب", has_computer),
#     ("وقت كافي", has_time),
#     ("الدافعية", is_motivated)
# ]

# all_conditions_met = all(condition[1] for condition in study_conditions)
# any_condition_failed = any(not condition[1] for condition in study_conditions)

# print(f"\nشروط الدراسة:")
# for condition_name, result in study_conditions:
#     status = "✅" if result else "❌"
#     print(f"  {status} {condition_name}: {'متوفر' if result else 'غير متوفر'}")

# print(f"\nجميع الشروط متوفرة: {all_conditions_met}")
# print(f"أي شرط مفقود: {any_condition_failed}")

# # ========================================
# # 3. أخذ المدخلات والتحقق المتقدم
# # ========================================

# print("\n⌨️ الدرس الثالث: أخذ المدخلات والتحقق المتقدم")
# print("-" * 50)

# # نظام تسجيل الطلاب
# print("📝 نظام تسجيل الطلاب:")

# student_id = input("أدخل رقم الطالب: ")
# student_name = input("أدخل اسم الطالب: ")
# student_grade = input("أدخل الدرجة (0-100): ")
# student_major = input("أدخل التخصص: ")

# # التحقق من صحة البيانات
# print(f"\n🔍 التحقق من صحة البيانات:")

# # فحص رقم الطالب
# if student_id.isdigit() and len(student_id) >= 3:
#     print(f"✅ رقم الطالب صحيح: {student_id}")
# else:
#     print(f"❌ رقم الطالب غير صحيح: {student_id}")

# # فحص الدرجة
# try:
#     grade_num = int(student_grade)
#     if 0 <= grade_num <= 100:
#         if grade_num >= 90:
#             grade_text = "ممتاز"
#         elif grade_num >= 80:
#             grade_text = "جيد جداً"
#         elif grade_num >= 70:
#             grade_text = "جيد"
#         elif grade_num >= 60:
#             grade_text = "مقبول"
#         else:
#             grade_text = "راسب"
#         print(f"✅ الدرجة صحيحة: {grade_num} ({grade_text})")
#     else:
#         print(f"❌ الدرجة خارج النطاق: {grade_num}")
# except ValueError:
#     print(f"❌ الدرجة غير صحيحة: {student_grade}")

# # فحص اسم الطالب
# if len(student_name) >= 3 and student_name.replace(" ", "").isalpha():
#     print(f"✅ اسم الطالب صحيح: {student_name}")
# else:
#     print(f"❌ اسم الطالب غير صحيح: {student_name}")

# # فحص التخصص
# if len(student_major) >= 2:
#     print(f"✅ التخصص صحيح: {student_major}")
# else:
#     print(f"❌ التخصص قصير جداً: {student_major}")

# # ========================================
# # 4. الجمل الشرطية الإبداعية
# # ========================================

# print("\n🔍 الدرس الرابع: الجمل الشرطية الإبداعية")
# print("-" * 50)

# # نظام تقييم الطلاب الذكي
# print("🎓 النظام الذكي لتقييم الطلاب:")

# # محاكاة بيانات الطالب
# student_score = 85
# attendance_rate = 95
# assignment_completed = True
# exam_passed = True

# print(f"📊 بيانات الطالب:")
# print(f"  الدرجة: {student_score}")
# print(f"  نسبة الحضور: {attendance_rate}%")
# print(f"  الواجبات مكتملة: {assignment_completed}")
# print(f"  الامتحان نجح: {exam_passed}")

# # تحليل ذكي متعدد الأبعاد
# print(f"\n🧠 التحليل الذكي:")

# # تحليل الدرجة
# if student_score >= 95:
#     grade_level = "ممتاز جداً"
#     recommendation = "منحة دراسية"
# elif student_score >= 85:
#     grade_level = "ممتاز"
#     recommendation = "تشجيع إضافي"
# elif student_score >= 75:
#     grade_level = "جيد جداً"
#     recommendation = "دعم أكاديمي"
# elif student_score >= 65:
#     grade_level = "جيد"
#     recommendation = "مراجعة إضافية"
# else:
#     grade_level = "يحتاج تحسين"
#     recommendation = "دعم مكثف"

# print(f"  مستوى الدرجة: {grade_level}")
# print(f"  التوصية: {recommendation}")

# # تحليل السياق
# context_score = 0
# context_factors = []

# if attendance_rate >= 90:
#     context_score += 20
#     context_factors.append("حضور ممتاز")
# elif attendance_rate >= 80:
#     context_score += 10
#     context_factors.append("حضور جيد")
# else:
#     context_score -= 10
#     context_factors.append("حضور ضعيف")

# if assignment_completed:
#     context_score += 15
#     context_factors.append("واجبات مكتملة")
# else:
#     context_score -= 15
#     context_factors.append("واجبات غير مكتملة")

# if exam_passed:
#     context_score += 25
#     context_factors.append("نجح في الامتحان")
# else:
#     context_score -= 25
#     context_factors.append("راسب في الامتحان")

# # تحليل نهائي
# final_score = student_score + context_score

# print(f"\n🎯 التحليل النهائي:")
# print(f"  الدرجة الأساسية: {student_score}")
# print(f"  عوامل السياق: {context_factors}")
# print(f"  نقاط السياق: {context_score}")
# print(f"  الدرجة النهائية: {final_score}")

# if final_score >= 100:
#     print("  🏆 طالب مميز! يستحق التقدير الخاص!")
# elif final_score >= 85:
#     print("  🎉 طالب ممتاز! أداء رائع!")
# elif final_score >= 70:
#     print("  👍 طالب جيد! استمر في التقدم!")
# elif final_score >= 60:
#     print("  📚 طالب مقبول! يحتاج دعم إضافي!")
# else:
#     print("  📖 طالب يحتاج مساعدة! خطة تحسين مطلوبة!")

# # ========================================
# # 5. الحلقات التكرارية الإبداعية
# # ========================================

# print("\n🔄 الدرس الخامس: الحلقات التكرارية الإبداعية")
# print("-" * 50)

# # محاكاة نظام إدارة المدرسة
# print("🏫 محاكاة نظام إدارة المدرسة:")

# # بيانات الفصول الدراسية
# classrooms = [
#     {"id": 1, "name": "الصف الأول", "students": 25, "teacher": "أستاذ أحمد", "subject": "الرياضيات"},
#     {"id": 2, "name": "الصف الثاني", "students": 30, "teacher": "أستاذة فاطمة", "subject": "العلوم"},
#     {"id": 3, "name": "الصف الثالث", "students": 22, "teacher": "أستاذ محمد", "subject": "اللغة العربية"},
#     {"id": 4, "name": "الصف الرابع", "students": 28, "teacher": "أستاذة سارة", "subject": "اللغة الإنجليزية"},
#     {"id": 5, "name": "الصف الخامس", "students": 26, "teacher": "أستاذ علي", "subject": "التاريخ"}
# ]

# print("📊 تقرير الفصول الدراسية:")
# print("-" * 60)

# total_students = 0
# total_teachers = len(classrooms)

# for classroom in classrooms:
#     total_students += classroom["students"]
    
#     # تحديد حالة الفصل
#     if classroom["students"] >= 30:
#         status = "🚨 مكتظ"
#     elif classroom["students"] >= 25:
#         status = "📊 ممتلئ"
#     elif classroom["students"] >= 20:
#         status = "✅ مناسب"
#     else:
#         status = "📉 قليل"
    
#     print(f"🏫 {classroom['name']}")
#     print(f"   المدرس: {classroom['teacher']}")
#     print(f"   المادة: {classroom['subject']}")
#     print(f"   عدد الطلاب: {classroom['students']}")
#     print(f"   الحالة: {status}")
#     print()

# # إحصائيات شاملة
# average_students = total_students / len(classrooms)
# print(f"📈 الإحصائيات الشاملة:")
# print(f"إجمالي الطلاب: {total_students}")
# print(f"عدد المدرسين: {total_teachers}")
# print(f"متوسط الطلاب لكل فصل: {average_students:.1f}")

# # تحليل التوزيع
# print(f"\n📊 تحليل التوزيع:")
# if average_students >= 28:
#     print("🔴 كثافة عالية - قد تحتاج فصول إضافية")
# elif average_students >= 25:
#     print("🟡 كثافة متوسطة - توزيع جيد")
# else:
#     print("🟢 كثافة منخفضة - فصول مريحة")

# # محاكاة نظام الدرجات
# print(f"\n📚 محاكاة نظام الدرجات:")
# subjects = ["الرياضيات", "العلوم", "اللغة العربية", "اللغة الإنجليزية", "التاريخ"]
# student_grades = {}

# # توليد درجات عشوائية
# import random

# for subject in subjects:
#     grade = random.randint(60, 100)
#     student_grades[subject] = grade
    
#     # تحليل الدرجة
#     if grade >= 95:
#         symbol = "🏆"
#         level = "ممتاز جداً"
#     elif grade >= 85:
#         symbol = "🥇"
#         level = "ممتاز"
#     elif grade >= 75:
#         symbol = "🥈"
#         level = "جيد جداً"
#     elif grade >= 65:
#         symbol = "🥉"
#         level = "جيد"
#     else:
#         symbol = "📚"
#         level = "مقبول"
    
#     print(f"  {symbol} {subject}: {grade} ({level})")

# # حساب المعدل
# average_grade = sum(student_grades.values()) / len(student_grades)
# print(f"\n📊 المعدل العام: {average_grade:.1f}")

# if average_grade >= 90:
#     overall_status = "🎓 تخرج بتقدير ممتاز"
# elif average_grade >= 80:
#     overall_status = "🎉 تخرج بتقدير جيد جداً"
# elif average_grade >= 70:
#     overall_status = "👏 تخرج بتقدير جيد"
# else:
#     overall_status = "📖 يحتاج تحسين"

# print(f"📈 التقدير النهائي: {overall_status}")

# # ========================================
# # 6. القوائم المتقدمة والتلاعب
# # ========================================

# print("\n📋 الدرس السادس: القوائم المتقدمة والتلاعب")
# print("-" * 50)

# # إدارة قائمة المواد الدراسية
# print("📚 إدارة قائمة المواد الدراسية:")

# # قوائم المواد المصنفة
# math_subjects = ["الجبر", "الهندسة", "الإحصاء", "التفاضل", "التكامل"]
# science_subjects = ["الفيزياء", "الكيمياء", "الأحياء", "الجيولوجيا", "علم الفلك"]
# language_subjects = ["العربية", "الإنجليزية", "الفرنسية", "الألمانية", "الإسبانية"]
# social_subjects = ["التاريخ", "الجغرافيا", "الفلسفة", "علم النفس", "علم الاجتماع"]

# # دمج جميع المواد
# all_subjects = math_subjects + science_subjects + language_subjects + social_subjects
# print(f"إجمالي المواد: {len(all_subjects)}")

# # تصنيف المواد حسب الصعوبة
# easy_subjects = []
# medium_subjects = []
# hard_subjects = []

# for subject in all_subjects:
#     if subject in ["الجبر", "التاريخ", "الجغرافيا", "العربية"]:
#         easy_subjects.append(subject)
#     elif subject in ["الهندسة", "الفيزياء", "الكيمياء", "الإنجليزية"]:
#         medium_subjects.append(subject)
#     else:
#         hard_subjects.append(subject)

# print(f"\n📊 تصنيف المواد حسب الصعوبة:")
# print(f"مواد سهلة: {len(easy_subjects)}")
# print(f"مواد متوسطة: {len(medium_subjects)}")
# print(f"مواد صعبة: {len(hard_subjects)}")

# # عرض المواد السهلة
# print(f"\n😊 المواد السهلة:")
# for i, subject in enumerate(easy_subjects, 1):
#     print(f"  {i}. {subject}")

# # مثال تطبيقي: تحليل سجل الحضور
# print(f"\n📊 تحليل سجل الحضور:")
# attendance_records = [
#     "2024-01-15 08:30:00 INFO حضور - طالب:أحمد - مادة:الرياضيات",
#     "2024-01-15 09:15:00 WARNING تأخير - طالب:فاطمة - مادة:العلوم",
#     "2024-01-15 10:00:00 INFO حضور - طالب:محمد - مادة:العربية",
#     "2024-01-15 10:45:00 ERROR غياب - طالب:سارة - مادة:الإنجليزية",
#     "2024-01-15 11:30:00 INFO حضور - طالب:علي - مادة:التاريخ",
#     "2024-01-15 12:15:00 WARNING تأخير - طالب:أحمد - مادة:الفيزياء",
#     "2024-01-15 13:00:00 INFO حضور - طالب:فاطمة - مادة:الكيمياء",
#     "2024-01-15 13:45:00 INFO حضور - طالب:محمد - مادة:الجغرافيا"
# ]

# # تحليل السجل
# present_students = []
# late_students = []
# absent_students = []
# unique_students = []
# unique_subjects = []

# for record in attendance_records:
#     parts = record.split(" - ")
#     time_info = parts[0]
#     status_info = parts[1]
#     student_info = parts[2]
    
#     # استخراج المعلومات
#     status = status_info.split()[0]
#     student = student_info.split(":")[1]
#     subject = parts[3].split(":")[1] if len(parts) > 3 else "غير محدد"
    
#     # تصنيف الحضور
#     if status == "حضور":
#         present_students.append(student)
#         print(f"✅ {student} حضر {subject}")
#     elif status == "تأخير":
#         late_students.append(student)
#         print(f"⚠️ {student} تأخر في {subject}")
#     elif status == "غياب":
#         absent_students.append(student)
#         print(f"❌ {student} غاب عن {subject}")
    
#     # جمع الطلاب والمواد الفريدة
#     if student not in unique_students:
#         unique_students.append(student)
#     if subject not in unique_subjects and subject != "غير محدد":
#         unique_subjects.append(subject)

# print(f"\n📈 إحصائيات الحضور:")
# print(f"  حضور: {len(present_students)}")
# print(f"  تأخير: {len(late_students)}")
# print(f"  غياب: {len(absent_students)}")
# print(f"  طلاب فريدين: {len(unique_students)}")
# print(f"  مواد فريدة: {len(unique_subjects)}")

# print(f"\n👥 الطلاب الفريدين:")
# for student in unique_students:
#     print(f"  - {student}")

# print(f"\n📚 المواد الفريدة:")
# for subject in unique_subjects:
#     print(f"  - {subject}")

# # ========================================
# # 7. القواميس المتقدمة والتطبيقات
# # ========================================

# print("\n📚 الدرس السابع: القواميس المتقدمة والتطبيقات")
# print("-" * 50)

# # نظام إدارة الطلاب المتقدم
# print("👨‍🎓 نظام إدارة الطلاب المتقدم:")

# # قاعدة بيانات الطلاب المتقدمة
# students_database = {
#     "2024001": {
#         "full_name": "أحمد محمد علي",
#         "age": 20,
#         "major": "علوم الحاسب",
#         "email": "ahmed@university.edu",
#         "phone": "+966501234567",
#         "enrollment_date": "2024-01-15",
#         "last_login": "2024-01-15 09:30:00",
#         "login_count": 45,
#         "account_status": "active",
#         "grades": {
#             "math": 85,
#             "science": 92,
#             "arabic": 78,
#             "english": 88
#         },
#         "attendance_rate": 95.5,
#         "scholarship": True
#     },
#     "2024002": {
#         "full_name": "فاطمة أحمد سالم",
#         "age": 19,
#         "major": "الهندسة",
#         "email": "fatima@university.edu",
#         "phone": "+966509876543",
#         "enrollment_date": "2024-01-10",
#         "last_login": "2024-01-15 10:15:00",
#         "login_count": 38,
#         "account_status": "active",
#         "grades": {
#             "math": 96,
#             "science": 94,
#             "arabic": 89,
#             "english": 91
#         },
#         "attendance_rate": 98.2,
#         "scholarship": True
#     },
#     "2024003": {
#         "full_name": "محمد عبدالله",
#         "age": 21,
#         "major": "الأعمال",
#         "email": "mohammed@university.edu",
#         "phone": "+966507654321",
#         "enrollment_date": "2024-01-05",
#         "last_login": "2024-01-15 08:45:00",
#         "login_count": 52,
#         "account_status": "active",
#         "grades": {
#             "math": 72,
#             "science": 68,
#             "arabic": 85,
#             "english": 75
#         },
#         "attendance_rate": 87.3,
#         "scholarship": False
#     }
# }

# # عرض معلومات الطلاب
# print("👥 معلومات الطلاب:")
# for student_id, student_data in students_database.items():
#     print(f"\n🔹 الطالب: {student_id}")
#     print(f"  الاسم الكامل: {student_data['full_name']}")
#     print(f"  العمر: {student_data['age']}")
#     print(f"  التخصص: {student_data['major']}")
#     print(f"  البريد الإلكتروني: {student_data['email']}")
#     print(f"  آخر دخول: {student_data['last_login']}")
#     print(f"  عدد مرات الدخول: {student_data['login_count']}")
#     print(f"  حالة الحساب: {student_data['account_status']}")
#     print(f"  نسبة الحضور: {student_data['attendance_rate']}%")
#     print(f"  منحة دراسية: {'نعم' if student_data['scholarship'] else 'لا'}")
    
#     # عرض الدرجات
#     print(f"  الدرجات:")
#     for subject, grade in student_data['grades'].items():
#         print(f"    {subject}: {grade}")

# # تحليل الأداء الأكاديمي
# print(f"\n🔍 تحليل الأداء الأكاديمي:")
# for student_id, student_data in students_database.items():
#     grades = student_data['grades']
#     average_grade = sum(grades.values()) / len(grades)
    
#     print(f"\n📊 {student_data['full_name']}:")
#     print(f"  المعدل العام: {average_grade:.1f}")
    
#     if average_grade >= 90:
#         performance = "ممتاز جداً"
#         symbol = "🏆"
#     elif average_grade >= 80:
#         performance = "ممتاز"
#         symbol = "🥇"
#     elif average_grade >= 70:
#         performance = "جيد"
#         symbol = "🥈"
#     else:
#         performance = "يحتاج تحسين"
#         symbol = "📚"
    
#     print(f"  الأداء: {symbol} {performance}")
    
#     # تحليل الحضور
#     attendance = student_data['attendance_rate']
#     if attendance >= 95:
#         attendance_status = "ممتاز"
#     elif attendance >= 90:
#         attendance_status = "جيد جداً"
#     elif attendance >= 80:
#         attendance_status = "جيد"
#     else:
#         attendance_status = "يحتاج تحسين"
    
#     print(f"  الحضور: {attendance_status}")

# # البحث عن طلاب بحسب المعايير
# print("\n🔍 البحث المتقدم:")
# search_major = input("أدخل التخصص للبحث: ")

# matching_students = []
# for student_id, student_data in students_database.items():
#     if student_data['major'].lower() == search_major.lower():
#         matching_students.append(student_data['full_name'])

# if matching_students:
#     print(f"✅ تم العثور على {len(matching_students)} طالب(ة) في تخصص '{search_major}':")
#     for student in matching_students:
#         print(f"   - {student}")
# else:
#     print(f"❌ لم يتم العثور على طلاب في تخصص '{search_major}'")

# # نظام مراقبة الأداء المدرسي
# print(f"\n📊 نظام مراقبة الأداء المدرسي:")
# school_performance = {
#     "total_students": 1500,
#     "passed_students": 1350,
#     "failed_students": 150,
#     "average_grade": 78.5,
#     "attendance_rate": 92.3,
#     "scholarship_students": 120
# }

# # تحليل الأداء المدرسي
# print("🏫 تحليل الأداء المدرسي:")
# performance_data = school_performance

# pass_rate = (performance_data["passed_students"] / performance_data["total_students"]) * 100
# scholarship_rate = (performance_data["scholarship_students"] / performance_data["total_students"]) * 100

# print(f"  إجمالي الطلاب: {performance_data['total_students']}")
# print(f"  الطلاب الناجحون: {performance_data['passed_students']}")
# print(f"  الطلاب الراسبون: {performance_data['failed_students']}")
# print(f"  المعدل العام: {performance_data['average_grade']}")
# print(f"  نسبة النجاح: {pass_rate:.1f}%")
# print(f"  نسبة الحضور: {performance_data['attendance_rate']}%")
# print(f"  طلاب المنح: {performance_data['scholarship_students']}")
# print(f"  نسبة المنح: {scholarship_rate:.1f}%")

# # تقييم الأداء العام
# if pass_rate >= 90 and performance_data['attendance_rate'] >= 95:
#     overall_rating = "🏆 مدرسة ممتازة"
# elif pass_rate >= 80 and performance_data['attendance_rate'] >= 90:
#     overall_rating = "🥇 مدرسة جيدة جداً"
# elif pass_rate >= 70 and performance_data['attendance_rate'] >= 85:
#     overall_rating = "🥈 مدرسة جيدة"
# else:
#     overall_rating = "📚 مدرسة تحتاج تحسين"

# print(f"\n🎯 التقييم العام: {overall_rating}")

# # ========================================
# # ملخص الدرس
# # ========================================

# print("\n" + "=" * 50)
# print("🎯 ملخص ما تعلمناه اليوم:")
# print("=" * 50)
# print("1. ✅ أساسيات البرمجة وأنواع البيانات المتقدمة")
# print("2. ✅ العمليات الحسابية والمنطقية المعقدة")
# print("3. ✅ أخذ المدخلات والتحقق المتقدم")
# print("4. ✅ الجمل الشرطية الإبداعية مع التحليل الذكي")
# print("5. ✅ الحلقات التكرارية الإبداعية مع محاكاة النظام")
# print("6. ✅ القوائم المتقدمة مع التحليل الشامل")
# print("7. ✅ القواميس المتقدمة مع تطبيقات إدارة الطلاب")
# print("\n🐍 تهانينا! لقد أتممت أساسيات Python المتقدمة!")
# print("🎓 أنت الآن جاهز للانتقال إلى المستوى التالي - الدوال (Functions)!")
# print("=" * 50)

################################


class Car:
    def __init__(self,brand,color,model,engine,price,speed):
        self.brand = brand
        self.color = color
        self.model = model
        self.engine = engine
        self.price = price
        self.speed = speed
        
    def get_color(self):
        print(f"Car {self.brand} has color {self.color}")
        
    def get_speed(self):
        print(f"Speed is {self.speed}")
        
    def set_price(self,new_price):
        self.price += new_price
        
    def set_speed(self,new_speed):
        self.speed = new_speed    
        
    def car_info(self):
        print(f"Brand: {self.brand}") 
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")
        print(f"Engine: {self.engine}")    
        print(f"Price: {self.price}")
        print(f"Speed: {self.speed}")  
        
        
        
#######################################
class BankAccount:
    def __init__(self,account_name,balance,account_expire,phone_number):
        self.account_name = account_name
        self.balance = balance
        self.account_expire = account_expire
        self.phone_number = phone_number
        
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if amount < self.balance :
            self.balance -= amount   
        else : 
            print(f"Cannot do this operations")         
    
    
    def get_expired(self):
        return self.account_expire            