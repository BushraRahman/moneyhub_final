import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from dbConnect import DBConnect
import pymongo
from bson.objectid import ObjectId
from pydantic import BaseModel


#used to get OpenAI API key
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
collections = pymongo.MongoClient(MONGODB_URI)["moneyhub_sessions"]
topics = collections["topics"]
cursor = topics.find_one({"_id": ObjectId("66d4f34a16359626940dd878")})

# #remember that both preresponses and postresponses are optional
# session = """{
#   "_id": {
#     "$oid": "66db4e2296fe6f880287ca08"
#   },
#   "session_id": "session_1725648418392",
#   "session_url": "http://localhost:3000/session_1725648418392",
#   "session_qr": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJQAAACUCAYAAAB1PADUAAAAAklEQVR4AewaftIAAAS4SURBVO3BQY4cSRIEQbVA/f/Lun30UwCJ9GpyuCYSf1C15FC16FC16FC16FC16FC16FC16FC16FC16FC16FC16FC16FC16FC16FC16FC16MNLSfhNKt+UhCdUnkjCjcqUhN+k8sahatGhatGhatGHZSqbkvBEEiaVKQk3KlMSbpLwhMqUhCdUNiVh06Fq0aFq0aFq0YcvS8ITKk8kYVKZkjCp3CRhUpmScKNyk4RNSXhC5ZsOVYsOVYsOVYs+/ONUnlC5UZmSMCVhUrlR+ZccqhYdqhYdqhZ9+Mck4QmVJ5Iwqdwk4f/JoWrRoWrRoWrRhy9T+ZNUpiS8ofKEyjep/E0OVYsOVYsOVYs+LEvCn6QyJWFSmZIwqUxJmFSmJEwqUxImlSkJk8pNEv5mh6pFh6pFh6pFH15S+ZskYZPKlIQnVG5UblT+Sw5Viw5Viw5Vi+IPXkjCpDIlYZPKTRKeUHkiCU+o3CRhUpmSsEnlmw5Viw5Viw5Vi+IPvigJT6jcJOFGZUrCGyqbkjCpTEl4Q+WJJEwqbxyqFh2qFh2qFn14KQmTyqTyRhJuVKYkTCpTEiaVKQlTEjapvKEyJeENlU2HqkWHqkWHqkUfliVhUnlDZZPKEypTEm5UNqlMSZhUnkjCpLLpULXoULXoULXowzKVmyR8k8obKlMSJpWbJEwqN0mYVG5UbpJwo/JNh6pFh6pFh6pF8Qd/UBImlZskTCq/KQmTyhNJmFSmJLyhMiVhUpmSMKm8cahadKhadKhaFH/wF0vCN6lsSsKNyhNJeEJlSsKk8k2HqkWHqkWHqkUfviwJNypTEiaVKQk3KjdJeCIJT6h8k8qUhBuVKQmTyqZD1aJD1aJD1aL4gy9KwqTyRBImlSkJT6h8UxImlZskTCqbkjCpfNOhatGhatGhatGHl5IwqTyRhBuVG5WbJDyRhBuVJ5Jwo3KThG9KwqTyxqFq0aFq0aFq0YcvU5mS8EQSJpW/mcqUhEllSsKNypSESWVKwhMqmw5Viw5Viw5Viz58WRJuVKYkTCo3SZhUbpLwhMqUhBuVSWVKwqRyk4RJZUrCpHKThEll06Fq0aFq0aFqUfzBC0mYVKYkfJPKG0mYVKYkvKFyk4RNKlMSnlB541C16FC16FC1KP7gPywJk8oTSZhU3kjCGypPJGGTyhuHqkWHqkWHqkUfXkrCb1KZVG6SMKlMKk8kYVK5UZmS8EQSJpU3VL7pULXoULXoULXowzKVTUm4ScKkMqncJGFSmZLwhMqNypSEG5U3VKYk3Ki8cahadKhadKha9OHLkvCEyqYkvKEyJWFKwo3KE0l4Q2VKwqQyJWHToWrRoWrRoWrRh39MEiaVKQmTypSEJ1SmJExJmFRuVN5IwhMqmw5Viw5Viw5Viz78Y1RuVG5UbpIwJeFG5Y0kPKFyk4RJZdOhatGhatGhatGHL1P5JpUnknCjMiVhUpmSMKlMSXhDZUrCpDIlYVL5TYeqRYeqRYeqRR+WJeE3JeFG5Q2VN1SeSMKk8oTKlIRJ5ZsOVYsOVYsOVYviD6qWHKoWHaoWHaoWHaoWHaoWHaoWHaoWHaoWHaoWHaoWHaoWHaoWHaoWHaoWHaoW/Q96zkD+mkYa2AAAAABJRU5ErkJggg==",
#   "topic_id": "4",
#   "students": [
#     {
#       "student_id": "student_001",
#       "name": "John Doe",
#       "target_sub_topics": [
#         "Visualizing Goals",
#         "Understanding Values"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "A"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     },
#     {
#       "student_id": "student_002",
#       "name": "Jane Smith",
#       "target_sub_topics": [
#         "Setting SMART Goals",
#         "Analyzing Goals"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     },
#     {
#       "student_id": "student_003",
#       "name": "Michael Johnson",
#       "target_sub_topics": [
#         "Visualizing Goals",
#         "Analyzing Goals"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "A"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "B"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     },
#     {
#       "student_id": "student_004",
#       "name": "Emily Davis",
#       "target_sub_topics": [
#         "Understanding Values",
#         "Setting SMART Goals"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "A"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     },
#     {
#       "student_id": "student_005",
#       "name": "David Brown",
#       "target_sub_topics": [
#         "Visualizing Goals",
#         "Understanding Values"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "B"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     },
#     {
#       "student_id": "student_006",
#       "name": "Sophia Martinez",
#       "target_sub_topics": [
#         "Setting SMART Goals",
#         "Analyzing Goals"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     },
#     {
#       "student_id": "student_007",
#       "name": "Chris Wilson",
#       "target_sub_topics": [
#         "Visualizing Goals",
#         "Understanding Values"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     },
#     {
#       "student_id": "student_008",
#       "name": "Isabella Garcia",
#       "target_sub_topics": [
#         "Setting SMART Goals",
#         "Analyzing Goals"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "A"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "B"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     },
#     {
#       "student_id": "student_009",
#       "name": "Ethan Lee",
#       "target_sub_topics": [
#         "Visualizing Goals",
#         "Setting SMART Goals"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     },
#     {
#       "student_id": "student_010",
#       "name": "Olivia Clark",
#       "target_sub_topics": [
#         "Understanding Values",
#         "Analyzing Goals"
#       ],
#       "pre_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "B"
#         }
#       ],
#       "post_quiz_answers": [
#         {
#           "question_id": "1",
#           "selected_option_id": "C"
#         },
#         {
#           "question_id": "2",
#           "selected_option_id": "B"
#         },
#         {
#           "question_id": "3",
#           "selected_option_id": "D"
#         },
#         {
#           "question_id": "4",
#           "selected_option_id": "A"
#         }
#       ]
#     }
#   ],
#   "insights": [
#     {
#       "quantitative": "36%",
#       "qualitative": "Increase of understanding",
#       "_id": {
#         "$oid": "66db56ab96fe6f880287cb1e"
#       }
#     },
#     {
#       "quantitative": "100%",
#       "qualitative": "Students understand SMART goals",
#       "_id": {
#         "$oid": "66db56ab96fe6f880287cb1f"
#       }
#     },
#     {
#       "quantitative": "85%",
#       "qualitative": "Improvement in financial literacy concepts",
#       "_id": {
#         "$oid": "66db56ab96fe6f880287cb20"
#       }
#     }
#   ],
#   "created_at": {
#     "$date": "2024-09-06T18:46:58.486Z"
#   },
#   "__v": 2
# }"""

# # Load the students' responses
student_data = json.loads(session)["students"]

trends_data = {}

# #test if it being optional works

letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3}
def byTopic3(topic_id):
    MONGODB_URI = os.getenv("MONGODB_URI")
    collections = pymongo.MongoClient(MONGODB_URI)["moneyhub_sessions"]
    topics = collections["topics"]
    topic = topics.find_one({"_id": ObjectId(topic_id)})
    topic_name = topic["name"]
    for i in range(0,4):
        sub_topic_name = topic["sub_topics"][i]
        sub_topic={}
        correct_choice = topic["quiz"][i]["correct_option_id"]
        sub_topic["correct_answer"] = topic["quiz"][i]["options"][letters_to_numbers[correct_choice]]["text"]
        correct_answer_count=0
        for student in student_data:
            student_arr={}
            if len(student["pre_quiz_answers"]) > 0:
                selected_option = student["pre_quiz_answers"][i]["selected_option_id"]
                student_arr["pre_response"] = topic["quiz"][i]["options"][letters_to_numbers[selected_option]]["text"]
                if len(student["post_quiz_answers"]) > 0:
                    selected_option = student["pre_quiz_answers"][i]["selected_option_id"]
                    student_arr["post_response"] = topic["quiz"][i]["options"][letters_to_numbers[selected_option]]["text"]
                    if (student_arr["pre_response"] == student_arr["post_response"] and student_arr["pre_response"] == sub_topic["correct_answer"]):
                        student_arr["progress"]="consistently correct"
                    elif(student_arr["pre_response"] == student_arr["post_response"] and student_arr["pre_response"] != sub_topic["correct_answer"]):
                      student_arr["progress"]="wrong"
                    elif(student_arr["pre_response"] != sub_topic["correct_answer"] and student_arr["post_response"] == sub_topic["correct_answer"]):
                        student_arr["progress"]="improved"
                    elif(student_arr["pre_response"] != sub_topic["correct_answer"] and student_arr["post_response"] != sub_topic["correct_answer"]):
                        student_arr["progress"]="different wrong answer"
                    else:
                        student_arr["progress"]="declined"
                else:
                    student_arr["progress"]="N/A"
            if (student_arr["post_response"] == sub_topic["correct_answer"]):
              correct_answer_count+=1
            #add the student dictionary to the sub-topic's dictionary
            sub_topic[student['name']] = student_arr
        sub_topic["average_score"] = 100 * float(correct_answer_count)/float(len(sub_topic)-1)
        #add the completed dictionary for a sub-topic to the actual dict
        trends_data[sub_topic_name] = sub_topic
    print(trends_data)

byTopic3("66d4f34a16359626940dd878")

example_json = """{ quantitative: "36%", qualitative: "Increase of understanding", "study_tools": {"book on college"}},
      { quantitative: "100%", qualitative: "Students understand SMART goals" },
      { quantitative: "85%", qualitative: "Improvement in financial literacy concepts" }"""

openai = OpenAI()

# topics_list = json.dumps(topics_data["credit_score"]["sub_topics"])

systemPrompt2 = f"""
    act as a financial educator, You are analyzing student performance across multiple sub-topics. Below is the data of students' pre- and post-responses along with if they were correct, the correct answers, and students' names:

    {trends_data}

    For each student's data in each sub-topic, the progress can be provided as 'wrong', 'consistently correct', 'improved', 'different wrong answer', or 'declined'.
    Use the progress provided for each student in each sub-topic and the average_score in each subo-topic to summarize the overall trends in understanding in each sub-topic, noting sub-topic where understanding has shown improvement,
    sub-topics where understanding is poor, and any general patterns observed. Note especially the sub-topics that need to be taught more.
    Give only overall trends, do not mention individual students.

     Act as a grant writer: create a performance report based on students' performance on the pre- and post-responses.
     Format the output as a JSON that has at least three insights, each insight having the quantitative percentage that the topic or sub-topic was understood by everyone,
     a qualitative observation about students' undertanding of a sub-topic or topic, and the two best study tools to improve understanding in that sub-topic.
     Example: 
     {example_json}
    """
userPrompt = "Please summarize the overall trends in students' understanding across each sub-topic. Discuss areas where students have shown significant improvement, areas of struggle, and any general patterns you observe."

class insight(BaseModel):
  quantitative: int
  qualitative: str
  study_tools: list[str]

class InsightGeneration(BaseModel):
  insights: list[insight]


completion = openai.beta.chat.completions.parse(
    model="gpt-4o-mini-2024-07-18",
    response_format=InsightGeneration,
    messages=[
        {"role": "system", "content": systemPrompt2},
        {
            "role": "user", "content": userPrompt
        }
    ]
)

result = completion.choices[0].message
print(result.parsed)

