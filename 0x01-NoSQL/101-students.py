#!/usr/bin/env python3
""" 101-main """

def top_students(mongo_collection):
    """ return all student sorted by avg score"""
    # bring th data
    student_data = []
    for student in mongo_collection.find():
        # default value would be empty list
        topics = student.get('topics', [])
        if topics:
            avg_score = 0
            for topic in topics:
                avg_score += topic.get('score', 0)
            average_score = avg_score / len(topics)

        new_student = {
          "_id": student['_id'],
          "name": student['name'],
          "averageScore": average_score
          }
        student_data.append(new_student)

    # sort  in descinding order
    student_data.sort(key=lambda x: x['averageScore'], reverse= True)
    return student_data
