from flask import Flask, render_template,request
from product import Product

app=Flask(__name__)

productlist=[]
@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/save/product", methods=["GET","POST"])
def save_product():
    message=''
    if request.method=="POST":
        formdata=request.form
        pid=int(formdata.get("pid"))
        isDublicate=False
        for prd in productlist:
            if prd.productID==pid:
                message="Dublicate Product "
                isDublicate = True
                break
        if isDublicate:
            message="Dublicate product"
        else:
            product=Product(pid=formdata.get("pid"),
                                    pnm=formdata.get("pnm"),
                                    pprice=formdata.get("price"),
                                    pven=formdata.get("pvae"),
                                    pqty=formdata.get("pqtty"))
            productlist.append(product)
            message="PRODUCT ADD SUCCEFULLY"


    return render_template("addproduct.html", result=message)

@app.route("/show/product")
def show_product():
    return render_template("showproduct.html",productlist=productlist)

def delete_product():
    pass

if __name__==("__main__"):
    app.run(debug=True)

