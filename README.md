## Level: 02 

- ### Admin Portal:
  - **Core data management:**

    - [x] Subject List - Dynamically managed (Default list - Physics, Maths, Botany, and Zoology).
    - [x] Category Tags - Dynamically managed (Will be added to the experiments and can be used for filtering purposes).

  - **Content Edit feature:**

    - [x] Content creation - While creating the content, in the Subject details option the list will be shown dynamically with respect to Core Data Management.

  - [x] Views count option. 

  - **Blog Page:**

    - [x] Add filters option.
    - [x] Provide Claps option to the viewers.
    - [ ] Sorting option based on Views and Claps.

  - [x] Frontend Improvements. 

## Get & Running on your Local Machine

- Clone the **Repo**
```sh
cd ~/Dev/
mkdir exp
cd exp
git clone  .
```
- Create a **Virtual Environment** for **Python**
	- using **Poetry**
	```python
	virtualenv --python=python3.9 .
	source bin/activate
	poetry install
	```
	- using **Virtualenv**
	```python
	python -m virtualenv --python=python3.9 .
	source bin/activate
	pip install -r requirements.txt
	```
	
- Run Locally
```python
cd ~/Dev/django_vercel
python manage.py runserver
```
