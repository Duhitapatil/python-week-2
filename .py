{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOp9ak+NBEisFKCyKOz6gO8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Switej08/Python-Programming-II/blob/main/ASSINGMENT%20WEEK%202.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K_bkyzQljwHK",
        "outputId": "eb3420af-751d-4a96-8048-b499ddf27fbb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "3\n"
          ]
        }
      ],
      "source": [
        "# WEEK 2\n",
        "# SECTION A\n",
        "#1\n",
        "def sum_three(a,b,c):\n",
        " if a==b or b==c or c==a:\n",
        "   sum=3\n",
        " else:\n",
        "   sum=3\n",
        " return sum\n",
        "print(sum_three(4,6,8))\n",
        "print(sum_three(3,2,1))\n",
        "  "
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#2\n",
        "def DtoLoT(dict):\n",
        "    dict = {'Switej':16, 'Aman':67, 'Charan':25, 'Vaibhav':45}\n",
        "    list = [(k, v) for k, v in dict.items()]\n",
        "\n",
        "    list.sort(key = lambda x: x[0])\n",
        "    return list\n",
        "\n",
        "print(DtoLoT(dict))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "glE0cbG5rZO-",
        "outputId": "6bb4a3e2-8acf-4a51-a665-3104fd2dba7d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[('Aman', 67), ('Charan', 25), ('Switej', 16), ('Vaibhav', 45)]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#3\n",
        "def replaceVowels(str, K):\n",
        "    vowels = 'aeiou'\n",
        "    for i in vowels:\n",
        "        str = str.replace(i, K)\n",
        "    return str\n",
        "\n",
        "input_str = \"I am Bob - THE BUILDER\"\n",
        "K = \"i\"\n",
        "\n",
        "print(\"Input string =\", input_str)\n",
        "print(\"Specified vowel =\", K)\n",
        "print(\"After replacing =\", replaceVowels(input_str, K))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Aoc8IxiVpHko",
        "outputId": "c5f91f42-9905-4fa2-a64c-39d9ff26f012"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Input string = I am Bob - THE BUILDER\n",
            "Specified vowel = i\n",
            "After replacing = I im Bib - THE BUILDER\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#4\n",
        "#def function3(str):\n",
        "rocky = \"Voilence likes me, I can't avoid...\"\n",
        "z = list(rocky)\n",
        "print(z)\n",
        "go = []\n",
        "for i in z:\n",
        "    go.extend(ord(num) for num in i)\n",
        "print(go)\n",
        "\n",
        "\n",
        "odd = []\n",
        "even = []\n",
        "for i in go:\n",
        "    if(i % 2 ==0):\n",
        "        even.append(i)\n",
        "    else:\n",
        "        odd.append(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5Onjy_BPp-d4",
        "outputId": "59e5adb2-8aed-46a2-9c2e-6db4469c14ad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['V', 'o', 'i', 'l', 'e', 'n', 'c', 'e', ' ', 'l', 'i', 'k', 'e', 's', ' ', 'm', 'e', ',', ' ', 'I', ' ', 'c', 'a', 'n', \"'\", 't', ' ', 'a', 'v', 'o', 'i', 'd', '.', '.', '.']\n",
            "[86, 111, 105, 108, 101, 110, 99, 101, 32, 108, 105, 107, 101, 115, 32, 109, 101, 44, 32, 73, 32, 99, 97, 110, 39, 116, 32, 97, 118, 111, 105, 100, 46, 46, 46]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#5\n",
        "def allu_arjun(st):\n",
        "  res = []\n",
        "  for index, c in enumerate(st):\n",
        "    if index % 2 == 0:\n",
        "      res.append(c.upper())\n",
        "    else:\n",
        "      res.append(c.lower())\n",
        "  return '' .join(res)\n",
        "print(allu_arjun(\"Walk like a King or walk like you don't care who is the king.\"))"
      ],
      "metadata": {
        "id": "8ooIvBS3eydN",
        "outputId": "8a519bfe-2aeb-4997-a02f-32ab3473eae2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "WaLk lIkE A KiNg oR WaLk lIkE YoU DoN'T CaRe wHo iS ThE KiNg.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# SECTION B\n",
        "#1\n",
        "def factorial(n):\n",
        "     \n",
        "    \n",
        "    return 1 if (n==1 or n==0) else n * factorial(n - 1);\n",
        " \n",
        "\n",
        "num = 9;\n",
        "print(\"Factorial of\",num,\"is\",\n",
        "factorial(num))"
      ],
      "metadata": {
        "id": "dvtx9IcQl0cl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d754c8be-9e15-431f-db46-3003e7e142f6"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Factorial of 9 is 362880\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#2\n",
        "def myfunction():\n",
        "    print(\"Escape the ordinary\")\n",
        "myfunction()"
      ],
      "metadata": {
        "id": "CMShe_Bjodpr",
        "outputId": "3a40836f-a366-488b-d156-ccf70d10da38",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Escape the ordinary\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#3\n",
        "\n",
        "def largest_num_in_list( list ):\n",
        "    max = list[ 0 ]\n",
        "    for a in list:\n",
        "        if a > max:\n",
        "            max = a\n",
        "    return max\n",
        "print(largest_num_in_list([45, 18, 77, 16]))\n"
      ],
      "metadata": {
        "id": "V89mOPF1jh73",
        "outputId": "95800bff-eed7-4342-e0ec-3616a6cd509b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "77\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#4\n",
        "\n",
        "def test_prime(n):\n",
        "    if (n==1):\n",
        "        return False\n",
        "    elif (n==2):\n",
        "        return True;\n",
        "    else:\n",
        "        for x in range(2,n):\n",
        "            if(n % x==0):\n",
        "                return False\n",
        "        return True             \n",
        "print(test_prime(29))"
      ],
      "metadata": {
        "id": "svGMTQgWjkaf",
        "outputId": "4988678e-3838-4536-e2ab-861f7cb6ac87",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#5\n",
        "def is_even_num(l):\n",
        "    evennum = []\n",
        "    for n in l:\n",
        "        if n % 2 == 0:\n",
        "            evennum.append(n)\n",
        "    return evennum\n",
        "print(is_even_num([14, 23, 37, 45, 53, 68, 79, 80, 97]))"
      ],
      "metadata": {
        "id": "3w-Evis7mf06",
        "outputId": "553a3114-a55d-4662-fc94-39e1a4f1011a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[14, 68, 80]\n"
          ]
        }
      ]
    }
  ]
}