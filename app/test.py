from app.db import User
u = User.query.filter(User.UserPhone.ilike('%'+'15'+'%')|User.NickName.ilike('%a%')).filter_by(UserSex=1).all()
print(u)


