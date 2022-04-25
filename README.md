# instructor_assessment
### A mini project built with Django (Python).
### Please do well to consume this API with an API tester, like POSTMAN

# API Documentation
Authentication Token Type - (JWT / Bearer)

- [Live Project's Base URL](http://crypticwisdom.pythonanywhere.com/) - [http://crypticwisdom.pythonanywhere.com/]

- [Sign-UP](http://crypticwisdom.pythonanywhere.com/account/sign-up/) - [http://crypticwisdom.pythonanywhere.com/account/sign-up/]
  - Method - POST
  - Parameters - (firstname, lastname, username, email, passoword, password_confirm)
  
- [Login](http://crypticwisdom.pythonanywhere.com/account/auth/jwt/create/) - [http://crypticwisdom.pythonanywhere.com/account/auth/jwt/create/]
  - Method - GET
  - Parameters (username, password)
  
- [Get a new Refresh Token](http://crypticwisdom.pythonanywhere.com/account/auth/jwt/refresh/) - [http://crypticwisdom.pythonanywhere.com/account/auth/jwt/refresh/]
  - Method - POST
  - Parameters - (refresh): refresh token gotten during login.
  
- [Create Post](http://crypticwisdom.pythonanywhere.com/post/create/) - [http://crypticwisdom.pythonanywhere.com/post/create/]
  - Method - POST
  - Parameter - (title, content)
  
- [Like Particular Post](http://crypticwisdom.pythonanywhere.com/post/like/<post-slug>/) - [http://crypticwisdom.pythonanywhere.com/post/like/<post-slug>/]
  - Method - POST
  - Parameter - (slug) post's unique identifier.
  
- [List Of All Post](http://crypticwisdom.pythonanywhere.com/post/list/) - [http://crypticwisdom.pythonanywhere.com/post/list/]
  - Method - GET
  - Parameter - No parameter
  
- [Delete a Post](http://crypticwisdom.pythonanywhere.com/post/delete/<post-slug>/) - [http://crypticwisdom.pythonanywhere.com/post/delete/<post-slug>/]
  - Method - Delete
  - Parameter - (slug) post's unique identifier.
  
- [Update a Post](http://crypticwisdom.pythonanywhere.com/post/update/<post-slug>/) - [http://crypticwisdom.pythonanywhere.com/post/update/<post-slug>/]
  - Method - PUT
  - Parameter - (slug) post's unique identifier.
 
