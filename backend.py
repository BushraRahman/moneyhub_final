import json
from openai import OpenAI
from dotenv import load_dotenv

#used to get OpenAI API key
load_dotenv()

topics = """{"credit_score": {
    "sub_topics": ["visualization","values","alternatives","budgeting"],
    "questions": {
        "q1": "What shouldn't you think about while visualizing?",
        "q2": "What are values?",
        "q3": "What does a SMART goal create for your goals?",
        "q4": "What helps you visualize the pros/cons of a goal?"
    },
    "choices": {
        "q1": ["creativity and fun", "your pet", "limitations or obstacles", "debt and savings"],
        "q2": ["what's important to your parents", "what's important to you", "your passion", "what's important to your friends"],
        "q3": ["an answer key", "a hack", "nothing", "a roadmap"],
        "q4": ["a t chart", "closing your eyes", "your friends", "I don't know, i wasn't paying attention"]
    },
    "answer": {
        "q1": "limitations or obstacles",
        "q2": "what's important to you",
        "q3": "a roadmap",
        "q4": "a t chart"
    }
    },
    {"Budgeting/banking": {
    "sub_topics": ["Budgeting","Banking","SmartGoals","Risk"],
    "questions": {
        "q1": "What are the 3 keys to budgeting?",
        "q2": "What is the safest way of storing your money?",
        "q3": "What is a big factor in compounding interest?",
        "q4": "How do you minimize risk on your investments?"
    },
    "choices": {
        "q1": ["spend, save, store", "build debt, savings, cars", "lower debts, save, acquire assets", "track, get frustrated, don't follow through"],
        "q2": ["giving it to your mom", "a bank account", "carrying cash", "stashing it under your mattress"],
        "q3": ["bank", "your values", "theft", "time"],
        "q4": ["by not investing", "watching the news", "by diversifying", "by crying"]
    },
    "answer": {
        "q1": "lower debts, save, acquire assets",
        "q2": "a bank account",
        "q3": "time",
        "q4": "by diversifying"
    }
    },
    }"""

# Load the topics and questions
topics_data = json.loads(topics)

#remember that both preresponses and postresponses are optional
#Rayan, student 1: gets everything right!
#Shane, student 2: half right [gets values and alternatives wrong, puts your passions and an answer key], everything right at the end
#Dwayne, student 3: everything wrong (your pet, closing eyes), gets q1/visualization right afterwards
#Jessica, student 4: half right [get q1/visualization and q2/values wrong], becomes more wrong afterwards bc they get q4/budgeting wrong
#Jirel, student 5: one wrong [q3/alternatives as a hack], doesn't improve
#Ally, student 6: visualization no change positive, values decline, alternatives no change negative, budgeting improvement
session = """{"id": "123",
"topicID": "A",
"url":"url",
"students": {
    "1": {
        "name":"Rayan",
        "school":"BGC",
        "preResponses":{
            "q1":"limitations or obstacles",
            "q2":"what's important to you",
            "q3":"a roadmap",
            "q4":"a t chart"
        },
        "postResponses":{
            "q1":"limitations or obstacles",
            "q2":"what's important to you",
            "q3":"a roadmap",
            "q4":"a t chart"
        },
        "target_topics": ["credit_score"]
    },
    "2": {
        "name":"Shane",
        "school":"BGC",
        "preResponses":{
            "q1":"limitations or obstacles",
            "q2":"your passion",
            "q3":"an answer key",
            "q4":"a t chart"
        },
        "postResponses":{
            "q1":"limitations or obstacles",
            "q2":"what's important to you",
            "q3":"a roadmap",
            "q4":"a t chart"
        },
        "target_topics": ["credit_score"]
    },
    "3": {
        "name":"Dwayne",
        "school":"BGC",
        "preResponses":{
            "q1":"your pet",
            "q2":"your passion",
            "q3":"an answer key",
            "q4":"closing your eyes"
        },
        "postResponses":{
            "q1":"limitations or obstacles",
            "q2":"what's important to you",
            "q3":"a roadmap",
            "q4":"a t chart"
        },
        "target_topics": ["credit_score"]
    },
    "4": {
        "name":"Jessica",
        "school":"BGC",
        "preResponses":{
            "q1":"your pet",
            "q2":"what's important to your parents",
            "q3":"a roadmap",
            "q4":"a t chart"
        },
        "postResponses":{
            "q1":"limitations or obstacles",
            "q2":"what's important to you",
            "q3":"a roadmap",
            "q4":"a t chart"
        },
        "target_topics": ["credit_score"]
    },
    "5": {
        "name":"Jirel",
        "school":"BGC",
        "preResponses":{
            "q1":"limitations or obstacles",
            "q2":"what's important to you",
            "q3":"a hack",
            "q4":"a t chart"
        },
        "postResponses":{
            "q1":"limitations or obstacles",
            "q2":"what's important to you",
            "q3":"a roadmap",
            "q4":"a t chart"
        },
        "target_topics": ["credit_score"]
    },
    "6": {
        "name":"Ally",
        "school":"BGC",
        "preResponses":{
            "q1":"limitations or obstacles",
            "q2":"what's important to you",
            "q3":"nothing",
            "q4":"your friends"
        },
        "postResponses":{
            "q1":"limitations or obstacles",
            "q2":"what's important to you",
            "q3":"a roadmap",
            "q4":"a t chart"
        },
        "target_topics": ["credit_score"]
    }
}
}"""

# Load the students' responses
student_data = json.loads(session)["students"]

trends_data = {}

#test if it being optional works

def byTopic3(topic_name):
    for i in range(1,5):
        sub_topic_name = topics_data[topic_name]["sub_topics"][i-1]
        sub_topic={}
        sub_topic["correct_answer"] = topics_data[topic_name]["answer"][f"q{i}"]
        for student_index in student_data:
            student=student_data[student_index]
            student_arr={}
            if "preResponses" in student:
                    student_arr["pre_response"] = student["preResponses"][f"q{i}"]
                    if "postResponses" in student:
                        student_arr["post_response"] = student["postResponses"][f"q{i}"]
                        if (student["preResponses"][f"q{i}"] == student["postResponses"][f"q{i}"]):
                            student_arr["progress"]="consistently correct"
                        elif(student["preResponses"][f"q{i}"] != sub_topic["correct_answer"] and student["postResponses"][f"q{i}"] == sub_topic["correct_answer"]):
                            student_arr["progress"]="improved"
                        elif(student["preResponses"][f"q{i}"] != sub_topic["correct_answer"] and student["postResponses"][f"q{i}"] != sub_topic["correct_answer"]):
                            student_arr["progress"]="different wrong answer"
                        else:
                            student_arr["progress"]="declined"
                    else:
                        student_arr["progress"]="N/A"
            #add the student dictionary to the sub-topic's dictionary
            sub_topic[student['name']] = student_arr
        #add the completed dictionary for a sub-topic to the actual dict
        trends_data[topics_data[topic_name]["sub_topics"][i-1]] = sub_topic

byTopic3("credit_score")

openai = OpenAI()

topics_list = json.dumps(topics_data["credit_score"]["sub_topics"])

systemPrompt2 = f"""
    act as a financial educator, You are analyzing student performance across multiple sub-topics. Below is the data of students' pre- and post-responses along with if they were correct, the correct answers, and students' names:

    {trends_data}

    For each student's data in each sub-topic, the progress is provided as 'improved' or 'consistently correct'.
    Use the progress provided for each sub-topic for each student to summarize the overall trends in understanding in each sub-topic, noting sub-topic where understanding has shown improvement,
    sub-topics where understanding is poor, and any general patterns observed. Note especially the sub-topics that need to be taught more.
    Give only overall trends, do not mention individual students.

     Act as a grant writer: create a performance report based on students' performance on the pre- and post-responses.
    """
userPrompt = "Please summarize the overall trends in students' understanding across each sub-topic. Discuss areas where students have shown significant improvement, areas of struggle, and any general patterns you observe."

completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": systemPrompt2},
        {
            "role": "user", "content": userPrompt
        }
    ]
)
print(completion.choices[0].message)