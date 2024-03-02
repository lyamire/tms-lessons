from fastapi import FastAPI, HTTPException

from polls_models import Choice, Database as PollsDatabase, PaginatedQuestions, Question, QuestionVote
from shop_models import Database as ShopDatabase, Product, Category, PaginatedProducts, PaginatedCategories

app = FastAPI()
db_polls = PollsDatabase()
db_shop = ShopDatabase()

@app.get('/polls/questions')
def get_questions(ordering: str = '-pub_date',
                  page: int = 1,
                  page_size: int = 5) -> PaginatedQuestions:

    questions = db_polls.get_questions()[(page - 1) * page_size: page * page_size]
    return PaginatedQuestions(count=len(questions), results=questions)

@app.get('/polls/questions/{question_id}', responses={404: {}})
def get_question(question_id: int) -> Question:
    question = db_polls.get_question(question_id)
    if question is None:
        raise HTTPException(status_code=404, detail='Question does not exist')
    return question

@app.post('/polls/questions/{question_id}/vote', responses={404: {}})
def vote_question(question_id: int, question_vote: QuestionVote) -> Question:
    question: Question = db_polls.get_question(question_id)
    if question is None:
        raise HTTPException(status_code=404, detail=f'Question {question_id} does not exist')

    target_choice: Choice = next((x for x in question.choices if x.id == question_vote.choice_id), None)
    if target_choice:
        target_choice.votes += 1
        return question

    raise HTTPException(
        status_code=404, detail=f'Question {question_id} does not have choice {question_vote.choice_id}')

@app.get('/shop/products')
def get_products(page: int = 1, page_size: int = 5, category_id: int = 1) -> PaginatedProducts:
    products = db_shop.get_category_products(category_id)[(page - 1) * page_size: page * page_size]
    return PaginatedProducts(count=len(products), results=products, category_id=category_id)

@app.get('/shop/products/{product_id}')
def get_product(product_id: int) -> Product:
    product = db_shop.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail='Product does not exist')
    return product

@app.get('/shop/categories')
def get_categories(page: int = 1, page_size: int = 5, include_products: bool = False) -> PaginatedCategories:
    categories = db_shop.get_categories()[(page - 1) * page_size: page * page_size]

    if not include_products:
        categories = [Category(id=c.id, name=c.name, products=[]) for c in categories]

    return PaginatedCategories(count=len(categories), results=categories)

@app.get('/shop/categories/{category_id}')
def get_category(category_id: int, include_products: bool = False) -> Category:
    category = db_shop.get_category(category_id)

    if category is None:
        raise HTTPException(status_code=404, detail='Category does not exist')

    if not include_products:
        return Category(id=category.id, name=category.name, products=[])

    return category
