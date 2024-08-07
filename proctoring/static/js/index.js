const student_id = document.getElementById("student-id");
const assessment_id = document.getElementById("assessment-id");
const submitBtn = document.getElementById("submit-btn");
submitBtn.disable = true;


student_id.addEventListener('keydown', validate);
assessment_id.addEventListener('keydown', validate);

function validate(){
    if (student_id.value.trim().length > 0 && assessment_id.value.trim().length > 0){
        submitBtn.style.display = "block";
    }else{
        submitBtn.style.display = "none";
    }
    console.log('Writting...')
}