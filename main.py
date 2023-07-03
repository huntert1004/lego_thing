import requests
import pyperclip
import re

def find_similar_numbers(strings):
    pattern = r"\b\d+\b"
    numbers = set()
    for string in strings:
        matches = re.findall(pattern, string)
        numbers.update(matches)
    return numbers

def remove_long_numbers(numbers):
    short_numbers = []
    for number in numbers:
        if not (isinstance(number, str) and number.isdigit() and len(number) >= 5):
            short_numbers.append(number)
    return short_numbers

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None
    
def clean_strings(strings):
    cleaned_strings = []
    for string in strings:
        # Remove leading and trailing whitespace
        cleaned_string = string.strip()
        
        # Remove special characters
        cleaned_string = ''.join(char for char in cleaned_string if char.isalnum() or char.isspace())
        
        # Convert to lowercase
        cleaned_string = cleaned_string.lower()
        
        # Append cleaned string to the list
        cleaned_strings.append(cleaned_string)
    
    return cleaned_strings

url = "https://www.lego.com/en-us/bestsellers?sort.key=PRICE&sort.direction=DESC"
html_content = get_html(url)
pyperclip.copy(html_content)
titles = html_content.split('data-test="product-leaf-title"><span class="Markup__StyledMarkup-nc8x20-0 epIXnJ">')
prices = html_content.split('data-test="product-leaf-price">')
y=0
for x in titles:
    u = x.split('</span></span></a></div>')[0]
    titles[y] = u
    y+=1
del titles[0]
cleaned_strings = clean_strings(titles)
print(str(titles))
y=0
for x in prices:
    u = x.split('</span></span><div')[0]
    prices[y] = u
    y+=1
del prices[0]
print(str(prices))
images = html_content.split('<source type="image/webp" srcSet="')
y=0
for x in images:
    if y % 2 !=0:
        del images[y]
    
    y+=1
y=0
for x in images:
    u = x.split(' 1x,')[0]
    images[y] = u
    y+=1
if html_content:
    
    print("coppied:)")
    del images[0]
    
    # for x in range(len(images)):
    #     print(images[x])
    numbers_found = find_similar_numbers(images)

    if numbers_found:
        
        short_numbers = remove_long_numbers(numbers_found)
        for number in short_numbers:
            numbers_found.remove(number)
        
        y=0
        
        for number in images:
            if y % 4 != 0:
                print(y)
                del images[y]
            y+=1
        
        # for number in images:
        #     print(number)
            
            
        
        
        
    else:
        print("No numbers found in the strings.")
else:
    print("Failed to retrieve HTML content.")






