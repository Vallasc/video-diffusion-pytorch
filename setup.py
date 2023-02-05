from setuptools import setup, find_packages

setup(
  name = 'video-diffusion-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.6.0',
  license='MIT',
  description = 'Video Diffusion - Pytorch',
  long_description_content_type = 'text/markdown',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/video-diffusion-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'denoising diffusion probabilistic models',
    'video generation'
  ],
  install_requires=[
    'einops==0.4.0',
    'einops-exts==0.0.3',
    'rotary-embedding-torch==0.1.5',
    'torch==1.12',
    'torchvision',
    'tqdm'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
