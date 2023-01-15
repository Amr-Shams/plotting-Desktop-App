import pytest
import proc
@pytest.fixture
def app(qtbot):
    test_app=proc.inputing()
    qtbot.addWidget(test_app)
    return test_app
# test the labels
@pytest.fixture(autouse=True)
def first_app(app, request):
    request.instance.app = app

class  Test_firstPage_function:
    # test the function lablel
    def test_func_label(self,request):
        assert request.instance.app.namelabel.text()=="Function"
    # test the plot button text 
    def test_plot_button_Text(self,request):
        assert request.instance.app.plot_button.text()=="PLOT"
    def test_ClearButton_text(self,request):
        assert request.instance.app.clear_button.text()=="CLEAR"
    def test_function_line_text(self,request):
        assert request.instance.app.line.text()==""
    # tes the plot button sends a singal when clicked?
    def test_Clicked_plotButton(self,request,qtbot):
        with qtbot.waitSignal(request.instance.app.plot_button.clicked, timeout=1000):
            request.instance.app.plout_button.click()
    # check the error message appaer or not 
    def test_wrong_Equation(self,request):
        request.instance.app.line.setText("4x")
        request.instance.app.plot_button.click()
        assert request.instance.app.e.isVisible==True
    # check the second page is opend when the right eaution is ploted
    def test_ploted(self,request):
        request.instance.app.line.setText("x")
        request.instance.app.plot_button.click()
        assert request.instance.app.w.isVisible()==True
class Test_Min_button:
    #test the startup value of the x 
    def test_value(self,request):
        assert request.instance.app.mini.value() == -10
    def test_miniPossib_value(self,request):
        assert request.instance.app.mini.minimum()==-1000
    def test_maxPossib_value(self,request):
        assert request.instance.app.mini.maximum()==1000
    def test_prefix_label(self,request):
        assert request.instance.app.mini.prefix()=="-X: "

    def test_decreasing_value(self,request):
        request.instance.app.mini.stepBy(-1)
        assert request.instance.app.mini.value()==-11
    def test_increasing_value(self,request):
        request.instance.app.mini.stepBy(1)
        assert request.instance.app.mini.value()==-9
    def test_sendSingal_Onchange(self, request, qtbot):
        with qtbot.waitSignal(request.instance.app.mini.valueChanged, timeout=1000):
            request.instance.app.mn.stepBy(1)
    def test_error_toTheLimit(self,request):
        request.instance.app.mini.setValue(request.instance.app.maxi.value()+1)
        assert request.instance.app.e.isVisible()==True
    # do the same thing to maxi
class Test_Max_button:
    #test the startup value of the x 
    def test_value(self,request):
        assert request.instance.app.maxi.value() == 10
    def test_miniPossib_value(self,request):
        assert request.instance.app.maxi.minimum()==-1000
    def test_maxPossib_value(self,request):
        assert request.instance.app.maxi.maximum()==1000
    def test_prefix_label(self,request):
        assert request.instance.app.maxi.prefix()=="+X: "

    def test_decreasing_value(self,request):
        request.instance.app.maxi.stepBy(-1)
        assert request.instance.app.maxi.value()==9
    def test_increasing_value(self,request):
        request.instance.app.maxi.stepBy(1)
        assert request.instance.app.maxi.value()==11
    def test_sendSingal_Onchange(self, request, qtbot):
        with qtbot.waitSignal(request.instance.app.maxi.valueChanged, timeout=1000):
            request.instance.app.mn.stepBy(2)
    def test_error_toTheLimit(self,request):
        request.instance.app.maxi.setValue(request.instance.app.mini.value()-1)
        assert request.instance.app.e.isVisible()==True