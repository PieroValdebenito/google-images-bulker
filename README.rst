this is a fork of: google-images-download
#########################################

To build image

.. code::

  docker build . -t image-bulker

To run with docker:

.. code::

  docker run -p 8080:80 image-bulker:latest


Changes
=======
 - Added fastAPI with 3 endpoints: healthcheck, search, and clear temp files

Healthcheck
===========

GET /
200

.. code:: javascript

   {
    "api_status":"ok"
   }
 

Get images from google engine
=================================

GET /search?keywords=puppy&limit=2

Save the images in local and serve as static files until you clear temp files.

Check more input params following the documentation bellow!



Returns
200

.. code:: javascript

  {
  "images": {
         "puppy": [
              "/images/puppy/el-perro-1.jpg",
              "/images/puppy/el-perro-2.jpg"
           ]
      }
  }

Now the image will be available at: http://0.0.0.0:8080/images/puppy/el-perro-1.jpg

Note: many images may take longer, check logs for more info.

Clear temp files from local storage
==================================
GET /clear
200 

.. code:: javascript

  {
  "status": "ok"
  }


Google Images Download
######################

Python Script for 'searching' and 'downloading' hundreds of Google images to the local hard disk!

Documentation
=============

* `Documentation Homepage <https://google-images-download.readthedocs.io/en/latest/index.html>`__
* `Installation <https://google-images-download.readthedocs.io/en/latest/installation.html>`__
* `Input arguments <https://google-images-download.readthedocs.io/en/latest/arguments.html>`__
* `Examples and Code Samples <https://google-images-download.readthedocs.io/en/latest/examples.html#>`__


Disclaimer
==========

This program lets you download tons of images from Google.
Please do not download or use any image that violates its copyright terms.
Google Images is a search engine that merely indexes images and allows you to find them.
It does NOT produce its own images and, as such, it doesn't own copyright on any of them.
The original creators of the images own the copyrights.

Images published in the United States are automatically copyrighted by their owners,
even if they do not explicitly carry a copyright warning.
You may not reproduce copyright images without their owner'self permission,
except in "fair use" cases,
or you could risk running into lawyer'self warnings, cease-and-desist letters, and copyright suits.
Please be very careful before its usage! Use this script/code only for educational purposes.
