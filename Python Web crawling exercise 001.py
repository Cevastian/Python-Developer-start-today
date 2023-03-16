{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "9cfa1a08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pure value of result : 1.6666666666666667\n",
      "The value of tranc result : 1\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "no1 = 3\n",
    "no2 = 5\n",
    "print(\"Pure value of result :\", no2 / no1)\n",
    "print(\"The value of tranc result :\", math.trunc(no2/no1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "ff870449",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many data do you want to collect? 500\n",
      "You have to collect total 34 pages\n"
     ]
    }
   ],
   "source": [
    "count = int(input(\"How many data do you want to collect? \" ))\n",
    "page_cnt = math.ceil(count / 15)\n",
    "print(\"You have to collect total %s pages\" %page_cnt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "c9efc34e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Less than 4.9 and the nearest integer is 4.\n",
      "Less than 4.1 and the nearest integer is 4.\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "no1 = 4.9\n",
    "no2 = 4.1\n",
    "\n",
    "print(\"Less than %s and the nearest integer is %s.\" %(no1, math.floor(no1)))\n",
    "print(\"Less than %s and the nearest integer is %s.\" %(no2, math.floor(no2)))\n",
    "\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "d3e279a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It's easy to learn Python!\n",
      "t\n",
      "I\n"
     ]
    }
   ],
   "source": [
    "str1=\"It's easy to learn Python!\"\n",
    "print(str1)\n",
    "print(str1[1])\n",
    "print(str1[0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "a4b83b81",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "파이썬 \n"
     ]
    }
   ],
   "source": [
    "str1 =\"파이썬 최고!\"\n",
    "print(str1[0:4])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "a0a332cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "s easy to learn Python!\n",
      "It'\n"
     ]
    }
   ],
   "source": [
    "str1 = \"It's easy to learn Python!\"\n",
    "print(str1[3:])\n",
    "print(str1[:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "b71ab34d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python\n",
      "PYTHON\n"
     ]
    }
   ],
   "source": [
    "str2 = \"PyThoN\"\n",
    "print(str2.lower())\n",
    "print(str2.upper())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "bb860d1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<-- Left side spaces\n",
      "Right side spaces -->\n",
      "<-- Both sides spaces --->\n"
     ]
    }
   ],
   "source": [
    "str3 = \"     <-- Left side spaces\"\n",
    "str4 = \"Right side spaces -->    \"\n",
    "str5 =\"      <-- Both sides spaces --->     \"\n",
    "print(str3.lstrip())\n",
    "print(str4.rstrip())\n",
    "print(str5.strip())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "379aa59e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Is Shrimp a seafood?\n"
     ]
    }
   ],
   "source": [
    "str6 = \"Is shrimp chip a seafood?\"\n",
    "print(str6.replace(\"shrimp chip\", \"Shrimp\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "afdd3331",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['010', '1234', '5678']\n",
      "['010', '1234-5678']\n"
     ]
    }
   ],
   "source": [
    "tel = '010-1234-5678'\n",
    "print(tel.split('-'))\n",
    "print(tel.split('-',1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "06c5cc8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "str1 = \"I like Python!\"\n",
    "str2 = ['Python', 'webcrawler', 'Gachi labs']\n",
    "print(len(str1))\n",
    "print(len(str2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "6abe673d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "================================================================================\n",
      "Calculation exercise with string\n",
      "++++++++++++++++++++++++++++++++++++++++\n"
     ]
    }
   ],
   "source": [
    "print(\"=\" * 80)\n",
    "print(\"Calculation exercise with string\")\n",
    "print(\"+\" *40)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3b4e61de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1982-05-17', 'Park Gil Su', 30]\n"
     ]
    }
   ],
   "source": [
    "list1=['1982-05-17', 'Park Gil Su', 30]\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "eeff22e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['first', 'second', 'added by insert feature', 'third', 'added by append feature']\n"
     ]
    }
   ],
   "source": [
    "list2 = ['first', 'second', 'third']\n",
    "list2.append('added by append feature')\n",
    "list2.insert(2,'added by insert feature')\n",
    "print(list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0c00250e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "list before the deletion ['first', 'second', 'added by insert feature', 'third', 'added by append feature']\n",
      "list after the deletion ['first', 'second', 'third', 'added by append feature']\n",
      "list after remove feature ['first', 'second', 'third']\n"
     ]
    }
   ],
   "source": [
    "print('list before the deletion', list2)\n",
    "del list2[2]\n",
    "print('list after the deletion', list2)\n",
    "\n",
    "list2.remove('added by append feature')\n",
    "print('list after remove feature', list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e2f0e2e0",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After sorting by ascending order [1, 2, 3, 5, 8]\n",
      "After sorting by desending order [8, 5, 3, 2, 1]\n",
      "English sorting ['Apple', 'apple', 'banana', 'cherry']\n",
      "Korean sorting ['김유신', '이순신', '전우치', '홍길동']\n"
     ]
    }
   ],
   "source": [
    "list3 = [3, 1, 5, 8, 2]\n",
    "list3.sort()\n",
    "print('After sorting by ascending order', list3)\n",
    "\n",
    "list3.reverse()\n",
    "print('After sorting by desending order', list3)\n",
    "\n",
    "list4 = ['banana', 'apple', 'cherry', 'Apple']\n",
    "list4.sort()\n",
    "print(\"English sorting\", list4)\n",
    "\n",
    "list5 = ['홍길동', '전우치', '김유신', '이순신']\n",
    "list5.sort()\n",
    "print(\"Korean sorting\", list5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "dfe1febd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Currently, this course students are ['Hong Gil Dong', 'Il Ji Mae'] .\n",
      "Please input the first student name of adding this course list.Lee soon sin\n",
      "Lee soon sin student application was compoleted.\n",
      "Please input second student name of adding this course list.Kim jong seo\n",
      "Kim jong seo student application was compoleted.\n",
      "Currently, this course students are ['Hong Gil Dong', 'Il Ji Mae', 'Lee soon sin', 'Kim jong seo'] .\n"
     ]
    }
   ],
   "source": [
    "student = ['Hong Gil Dong', 'Il Ji Mae']\n",
    "print(\"Currently, this course students are %s .\" %student)\n",
    "\n",
    "student1 = (input(\"Please input the first student name of adding this course list.\"))\n",
    "print(\"%s student application was compoleted.\" %student1)\n",
    "student.append(student1)\n",
    "\n",
    "student2 = (input(\"Please input second student name of adding this course list.\"))\n",
    "print(\"%s student application was compoleted.\" %student2)\n",
    "student.append(student2)\n",
    "\n",
    "print(\"Currently, this course students are %s .\" %student)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ac2c2eea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Currently, this course students are ['Hong Gil Dong', 'Il Ji Mae', 'Lee soon sin'] .\n",
      "Please input student name for withdrawal of course application.Il Ji Mae\n",
      "Currently, this course students are ['Hong Gil Dong', 'Lee soon sin'] .\n"
     ]
    }
   ],
   "source": [
    "print(\"Currently, this course students are %s .\" %student)\n",
    "student3 = (input(\"Please input student name for withdrawal of course application.\"))\n",
    "student.remove(student3)\n",
    "student.sort()\n",
    "print(\"Currently, this course students are %s .\" %student)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "eb1bf85a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Currently this course applicators are Hong Gil Dong, Il Ji Mae, You Gwan Soon .\n"
     ]
    }
   ],
   "source": [
    "stu2 = 'Hong Gil Dong, Il Ji Mae, You Gwan Soon'\n",
    "print(\"Currently this course applicators are %s .\" %stu2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6d604700",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please input the name you want to change from: Il Ji Mae\n",
      "Please input the name you want to change to : Kim You Sin\n",
      "Hong Gil Dong, Il Ji Mae, You Gwan Soon\n",
      "We changed the name from Il Ji Mae to Kim You Sin .\n",
      "Currently applicators of this course are Hong Gil Dong, Kim You Sin, You Gwan Soon\n"
     ]
    }
   ],
   "source": [
    "ch_name1 = (input(\"Please input the name you want to change from: \"))\n",
    "ch_name2 = (input(\"Please input the name you want to change to : \"))\n",
    "\n",
    "stu2.replace(ch_name1, ch_name2)\n",
    "print(stu2)\n",
    "print(\"We changed the name from %s to %s .\" %(ch_name1,ch_name2))\n",
    "print(\"Currently applicators of this course are %s\" %(stu2.replace(ch_name1, ch_name2)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f822803b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
