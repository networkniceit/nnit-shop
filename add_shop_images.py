content = open('C:/NNIT-SHOP/index.html','r',encoding='utf-8').read()

imgs = {
    'HEADPHONES': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=400&fit=crop',
    'WATCH': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=400&fit=crop',
    'CAMERA': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400&h=400&fit=crop',
    'SPEAKER': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400&h=400&fit=crop',
    'JACKET': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=400&fit=crop',
    'SHOES': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=400&fit=crop',
    'GLASSES': 'https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=400&h=400&fit=crop',
    'TSHIRTS': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop',
    'COFFEE': 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400&h=400&fit=crop',
    'AIRPURE': 'https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400&h=400&fit=crop',
    'YOGAMAT': 'https://images.unsplash.com/photo-1601925228897-b7ed5e97c26b?w=400&h=400&fit=crop',
    'SHAKER': 'https://images.unsplash.com/photo-1593095948071-474c5cc2989d?w=400&h=400&fit=crop',
    'SKINCARE': 'https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400&h=400&fit=crop',
    'TOOTHBRUSH': 'https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?w=400&h=400&fit=crop',
    'TABLET': 'https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=400&h=400&fit=crop',
    'GAMES': 'https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?w=400&h=400&fit=crop',
    'ITEM': 'https://images.unsplash.com/photo-1560393464-5c69a73c5770?w=400&h=400&fit=crop',
}

imgs_js = 'var IMGS={' + ','.join(['"'+k+'":"'+v+'"' for k,v in imgs.items()]) + '};'
content = content.replace('var PRODUCTS =', imgs_js + '\nvar PRODUCTS =')

content = content.replace(
    "'<div class=\"product-img\">' +\n      p.icon +",
    "'<div class=\"product-img\"><img src=\"'+(IMGS[p.icon]||IMGS.ITEM)+'\" style=\"width:100%;height:100%;object-fit:cover\">' +"
)

content = content.replace(
    "'<div class=\"modal-img\">'+p.icon+'</div>'",
    "'<div class=\"modal-img\"><img src=\"'+(IMGS[p.icon]||IMGS.ITEM)+'\" style=\"width:100%;height:100%;object-fit:cover;border-radius:18px 0 0 18px\"></div>'"
)

content = content.replace(
    "'<div class=\"cart-item-img\">'+item.icon+'</div>'",
    "'<div class=\"cart-item-img\"><img src=\"'+(IMGS[item.icon]||IMGS.ITEM)+'\" style=\"width:64px;height:64px;object-fit:cover;border-radius:8px\"></div>'"
)

open('C:/NNIT-SHOP/index.html','w',encoding='utf-8').write(content)
print('DONE - real product images added!')
