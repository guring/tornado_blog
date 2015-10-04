This is my blog source code, powered by [Tornado][1] web framework.It's not yet a static blog generator, but it's really simple and lightweight,it has a blog engine must features, such as Category, Tag, Post, Page, Feed,now it's use sqlite3 database.

You need use Markdown markup language written post with your favorite editor, sign in blog and go to
`/post/new` post it.Picky type [post](www.baidu.com), just go to `/post/picky` upload your markdown file.

## Post Example

Post (see `example/post_example.md`):

    # Title

    - slug: title
    - published: 2012-06-26 19:00
    - tags: Test, Tornado, Python
    - category: Work

    ------------------------------

    This Content....

    ```python
    import math
    
    print math.sqrt(9)
    ```

Picky compare with Post,no tags, category and slug(see `picky` folder).

## Installation and Basic Usage 

Requirements:
>
1. [Tornado][1]
2. [misaka][2]
3. [pygments][3]

* Install required package: `pip install -r requirements.txt`
* Create Sqlite3 database: edit `tools.py` and `python tools.py -o createdb`