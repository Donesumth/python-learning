import requests
from bs4 import BeautifulSoup

def fetch_book_info(url):
    try:
        # 发送 HTTP 请求
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功

        # 解析 HTML
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("div", class_="info")  # 根据豆瓣页面结构调整

        book_list = []
        for book in books:
            title = book.find("a", title=True).get("title", "N/A").strip()
            author = book.find("div", class_="pub").text.strip() if book.find("div", class_="pub") else "N/A"
            rating = book.find("span", class_="rating_nums").text.strip() if book.find("span", class_="rating_nums") else "N/A"
            book_list.append({"title": title, "author": author, "rating": rating})

        return book_list

    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return []

if __name__ == "__main__":
    url = "https://book.douban.com/tag/小说"  # 示例：抓取“小说”标签下的图书
    books = fetch_book_info(url)
    for book in books:
        print(f"书名: {book['title']}, 作者/出版社: {book['author']}, 评分: {book['rating']}")