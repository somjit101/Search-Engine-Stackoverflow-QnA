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


## Design choices

In order to return the search results, there is a choice of entities in the dataset we choose to match with the query sentence, i.e. the text samples we consider in our [**StackSample Dataset**](https://www.kaggle.com/stackoverflow/stacksample) which would actually be matched/compared with the query string. Let us have a look at the possible options for this use case :

1. **Question *Titles* only**
2. **Question *Titles* + Question *Bodies* only**
3. **Question *Titles* + Question *Bodies* + Answer *Bodies***

Here, for simplicity and swift implementation, we match the query with the Question Titles in the dataset only. This can be easily upgraded to include the other options with some modifications. 


## Solution Approach

### Hashing + TF-IDF Scoring

This approach can be used for the **keyword-based search**. As we know, hashing refers to the technique of maintaining a collection of objects which can be indexed by a set of *keys*. Here, we break down the query sentence into individual words and create a hash table with each word being a key in it.  
Now, for the TF-IDF (Term Frequency - Inverse Document Frequency) score, we maintain the following Hashmaps :

* No. of occurences of each query word in the Questions where they are found in the dataset - **To Calculate Term Frequency**
* Set of the Questions where each query word is present - **To Calculate Inverse Document Frequency**. 

A combination of the above scores can be used to rank results returned in a keyword-based search.

### Semantic Similarity with Sentence Vectors

We know that any sentence of text can be represented in the form of a numerical vector which captures the semantic meaning of the passage/sentence. There are multiple methods of sentence vectorization including the use of Doc2Vec, SentenceBERT, Universal Sentence Encoder etc.   

As we store the vector represenetations of the questions in our dataset, we can simply calculate the value of some similarity measure between the query sentence and the questions so that the results can be ranked on the basis of closest semantic meaning with the query. 






