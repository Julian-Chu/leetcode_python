'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq


class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        if not results:
            return {}
        scores = {}

        for record in results:
            if record.id not in scores:
                scores[record.id] = []
            heapq.heappush(scores[record.id], record.score)
            if len(scores[record.id]) > 5:
                heapq.heappop(scores[record.id])

        student_avg = {}
        for student_id in scores:
            student_avg[student_id] = sum(scores[student_id]) / 5.0

        return student_avg


'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq


class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        if not results:
            return {}
        student_dict = {}
        for record in results:
            if record.id not in student_dict:
                student_dict[record.id] = []
            student_dict[record.id].append(record.score)

        average_score_dic = {}
        for student_id in student_dict:
            scores = student_dict[student_id]
            heap = []
            for score in scores:
                if len(heap) == 5:
                    if score > heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, score)
                else:
                    heapq.heappush(heap, score)
            average_score_dic[student_id] = sum(heap) / 5.0

        return average_score_dic


class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        students = {}

        for record in results:
            id, score = record.id, record.score
            if id not in students:
                students[id] = []

            if len(students[id]) < 5:
                heapq.heappush(students[id], score)
            else:
                heapq.heappushpop(students[id], score)

        high_five_avg = {}
        for id in students:
            avg = sum(students[id]) / 5.0
            high_five_avg[id] = avg

        return high_five_avg