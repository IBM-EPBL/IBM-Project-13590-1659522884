o

    �D^c�  �                   @   s�   d dl mZmZmZ ee�Ze�d�dd� �Ze�d�dd� �Ze�d�d	d
� �Z	e�d�dd
� �Z
edkr?ejddd� dS dS )�    )�Flask�render_template�url_for�/c                   C   �   t d�S )Nz
index.html�r   � r   r   �1D:\IBM\ASSIGNMENTS\ASSIGNMENT 4\Job-Portal\app.py�index   �   r
   z	/findajobc                   C   r   )Nz
findajob.htmlr   r   r   r   r	   �blog	   r   r   z/signupc                   C   r   )Nzsignup.htmlr   r   r   r   r	   �signup
   r   r
   z/signinc                   C   r   )Nzsignin.htmlr   r   r   r   r	   �signin   r   r   �__main__z0.0.0.0i�  )�host�portN)�flaskr   r   r   �__name__�app�router
   r   r
   r   �runr   r   r   r	   �<module>   s    



�