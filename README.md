# Stackoverflow Q&A Search Engine
An application to store a collection of questions and answers data found on Stackoverflow in an index using [ElasticSearch](https://www.elastic.co/) and perform a text search on the stored Q&amp;A's based on semantic meaning.


## Overview

All of us have found the solution to some technical issue on [StackOverflow](https://stackoverflow.com/), at some point in our professional career or during a learning phase in the field of software solution development. It is the single largest platform for professionals and programming enthusiasts share their knowledge on their individual areas of expertise, help fellow programmers who by answering questions/queries posted on the public forum and also to look for help on any challenges faced in their domain. 

### Problem Statement

As we are already aware, StackOverflow has a collection of Questions (characterised by a series of **keywords**) posted by users along with the answers to those questions posted by other users. Here, the problem statement is to design a **Search Engine** for the StackOverflow platform where the user can simply enter a query and the related questions along with the answers submitted to them (if any). 

To be practically feasible, the search engine needs to possess the following characteristics :

* **Both Keyword AND Semantic search** - The search engine needs to be capable of returning results 
* **Low Latency** - Typically <500 milliseconds
* **High Precision and Recall**
* **Low Computational/Server costs** - For feasibility of deployment and scalability


## Dataset 

Here, we use the [**StackSample Dataset**](https://www.kaggle.com/stackoverflow/stacksample) which contains about **10%** of the total questions and answers found on the StackOverflow website in text format. 

The Dataset contains 3 .csv files the details of which are as follows : 


* **Questions.csv** - 1.92 GB

  | Id  | OwnerUserId | CreationDate | ClosedDate | Score | Title | Body |
  |:---:|:-----------:|:------------:|:----------:|:-----:|:-----:|:----:|
  | ... | ...         | ...          | ...        | ...   | ...   | ...  |
  
  
* **Answers.csv** - 1.61 GB

  | Id  | OwnerUserId | CreationDate | ParentId | Score | Body |
  |:---:|:-----------:|:------------:|:--------:|:-----:|:----:|
  | ... | ...         | ...          | ...      | ...   | ...  |
  
  
* **Tags.csv** - 65.48 MB

  | Id  | Tag |
  |:---:|:---:|
  | ... | ... |
