import httpx
import re

class code():
    def __init__(self):
        self.codeIds = {
            "kotlin": 2960,
            "java": 10,
            "lua": 66,
            "nodejs": 22,
            "go": 21,
            "swift": 20,
            "rust": 19,
            "ruby": 13,
            "c#": 14,
            "c++": 12,
            "c": 11,
            "python": 9,
            "php": 1
        }
        self.otherName = {
            "kotlin": "kt",
            "java": "java",
            "lua": "lua",
            "nodejs": "node.js",
            "go": "go",
            "swift": "swift",
            "rust": "rs",
            "ruby": "rb",
            "c#": "cs",
            "c++": "cpp",
            "c": "c",
            "python": "py3",
            "php": "php"
        }
    
    async def run(self, language, code):
        try:
            codeId = self.codeIds[language]
        except KeyError:
            return '不支持的语言\n目前仅支持\nkotlin/java/lua/nodejs/go/swift/rust/ruby/c#/c++/c/py/php\n请输入全称'
        token = await self.getToken(codeId)
        result = await self.getResult(token, code, language)
        return result
    
    async def getToken(self, codeId):
        url = f"https://c.runoob.com/compile/{codeId}/"
        async with httpx.AsyncClient(verify=False, timeout=60, follow_redirects=True) as client:
            data = await client.get(url)
            result = data.text
        token = re.findall("token = '(.+)';", result)[0]
        return token
    
    async def getResult(self, token, code, language):
        language = self.otherName[language]
        data = {
            "code": code,
            "token": token,
            "stdin": '',
            "language": 7,
            "fileext": language
        }
        async with httpx.AsyncClient(verify=False, timeout=60, follow_redirects=True) as client:
            data = await client.post("https://tool.runoob.com/compile2.php", data=data)
            result = data.json()['output']
        return result
        

