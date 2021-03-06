from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, FormView, View
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from SCAM.scam.forms import CreateUserForm, ConnectForm
from django.contrib.auth.models import User
from SCAM.scam.models import Student, Course, Instructor, ActiveCourse, Review, PastCourse, CurrentCourse, FutureCourse, Friend, Connect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProfileRedirectView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        student = Student.objects.filter(sid=request.user.username).first()
        return HttpResponseRedirect(reverse('students', args=[student.id]))


class SignUpView(FormView):
    form_class = CreateUserForm
    template_name = 'signup.html'

    def get_success_url(self):
        user = self.get_form().save(commit=False)
        student = Student.objects.filter(sid=user.username).first()
        return reverse('students', args=[student.id])


class LandingView(TemplateView):
  template_name = 'landing.html'

class StudentView(DetailView):
    model = Student
    template_name = 'current_courses.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # uncomment this if you dont want to allow students to see other students profile page
        '''
        if request.user.student != self.object:
          return HttpResponseRedirect(<maybe access denied page?>)
        '''
        return super(StudentView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        try:
          context['active_score'] = float(self.object.days_active)/float(self.object.days_joined)*float(100)
        except ZeroDivisionError as e:
          context['active_score'] = 100
        context['current_courses'] = CurrentCourse.objects.filter(student=self.object)
        context['friend'] = Friend.objects.filter(friendA=self.object).first()
        return context

class PastCourseView(DetailView):
    model = Student
    template_name = 'past_courses.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(PastCourseView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PastCourseView, self).get_context_data(**kwargs)
        try:
            context['active_score'] = float(self.object.days_active)/float(self.object.days_joined)*float(100)
        except ZeroDivisionError as e:
            context['active_score'] = 100
        context['past_courses'] = PastCourse.objects.filter(student=self.object)
        return context

class FutureCourseView(DetailView):
    model = Student
    template_name = 'future_courses.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(FutureCourseView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FutureCourseView, self).get_context_data(**kwargs)
        try:
            context['active_score'] = float(self.object.days_active)/float(self.object.days_joined)*float(100)
        except ZeroDivisionError as e:
            context['active_score'] = 100
        context['future_courses'] = FutureCourse.objects.filter(student=self.object)
        return context


class FriendView(DetailView):
    model = Friend
    template_name = 'friends.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(FriendView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FriendView, self).get_context_data(**kwargs)
        print 'self.object', self.object
        context['friends'] = Friend.objects.filter(friendA=self.object)
        return context


class InstructorView(DetailView):
    model = Instructor
    template_name = 'instructor.html'

    def get_context_data(self, **kwargs):
        context = super(InstructorView, self).get_context_data(**kwargs)
        return context


class CourseView(DetailView):
    model = ActiveCourse
    template_name = 'course.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(CourseView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        courses = CurrentCourse.objects.filter(course=self.object)
        context['course_info'] = courses.first().course
        context['students'] = [course.student for course in courses]
        context['student'] = self.request.user.student
        return context


class ConnectView(FormView):
    model = Connect
    template_name = 'connect.html'
    form_class = ConnectForm
    success_url = 'results/'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(ConnectView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ConnectView, self).get_context_data(**kwargs)
        context['form'] = ConnectForm
        return context


class ConnectResultsView(FormView):
    template_name = 'connect_results.html'
    form_class = ConnectForm
    success_url = 'results/'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(ConnectResultsView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ConnectResultsView, self).get_context_data(**kwargs)
        return context


class ReviewView(ListView):
    model = Review
    template_name = 'reviews.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(ReviewView, self).get(request, *args, **kwargs)


class ReportView(ListView):
    model = PastCourse
    template_name = 'reporting.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(ReportView, self).get(request, *args, **kwargs)
