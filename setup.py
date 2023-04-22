import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
  long_description = fh.read()

setuptools.setup(
  name="nonebot-plugin-coderun",
  version="0.0.1",
  author="Yincmewy",
  author_email="2025173673@qq.com",
  description="基于runoob.com的在线代码运行插件",
  long_description=long_description,
  install_requires=[
          'nonebot2', 'nonebot-adapter-onebot', 'httpx', 'setuptools'
      ],
  long_description_content_type="text/markdown",
  url="https://github.com/Yincmewy/nonebot_plugin_coderun",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)
