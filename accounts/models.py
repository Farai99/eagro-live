from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    EDUCATION_CHOICES = (
        ('Graduated', 'Graduated'),
        ('A level', 'A level'),
        ('O level', 'O level'),
        ('Primary level', 'Primary level')
    )

    DEDICATION_CHOICES = (
        ('Full time', 'Full time'),
        ('Part time', 'Part time')
    )
    ACCOMMODATION_CHOICES = (
        ('Owner', 'Owner'),
        ('Renting', 'Renting'),
    )

    INCOME_CHOICES = (
        ('Salary', 'Salary'),
        ('Self employed', 'Self employed'),
        ('None', 'No Source of income')
    )
    DISEASES_CHOICES = (
        ('Low', 'Low'),
        ('Mild', 'Mild'),
        ('Severe', 'Severe')
    )
    DRAINAGE_CHOICES = (
        ('Low', 'Low'),
        ('High', 'High'),
    )
    SOIL_CHOICES = (
        ('Clay', 'Clay'),
        ('Loom', 'Loom'),
        ('Sand', 'Sand'),
    )
    LAND_CHOICES = (
        ('Owner', 'Owner'),
        ('Renting', 'Renting'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="img.png", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    education_level = models.CharField(max_length=20, null=True, choices=EDUCATION_CHOICES)
    dedication = models.CharField(max_length=20, null=True, choices=DEDICATION_CHOICES)
    accommodation_status = models.CharField(max_length=50, null=True, choices=ACCOMMODATION_CHOICES)
    household_size = models.IntegerField(default=1)
    experience_in_farming = models.PositiveIntegerField(default=0)

    # FinancialData
    total_current_debt = models.FloatField(default=0)
    average_monthly_earnings = models.FloatField(default=0)
    annual_or_season_turnover = models.FloatField(default=0)
    most_recent_annual_or_season_profit = models.FloatField(default=0)
    alternative_source_of_income = models.CharField(max_length=50, null=True, choices=INCOME_CHOICES)

    # WeatherData
    average_temperature = models.FloatField(default=0)
    moisture_levels = models.PositiveIntegerField(default=0)
    altitude = models.IntegerField(default=0)
    drought_frequencies_in_past_10_years = models.PositiveIntegerField(default=0)
    floods_frequencies_in_past_10_years = models.PositiveIntegerField(default=0)
    pest_and_diseases_frequency = models.CharField(max_length=20, null=True, choices=DISEASES_CHOICES)

    # SoilData
    soil_type = models.CharField(max_length=20, choices=SOIL_CHOICES,null=True)
    water_content = models.PositiveIntegerField(default=0)
    temperature = models.IntegerField(default=0)
    potassium_levels = models.IntegerField(default=0)
    nitrogen_Levels = models.IntegerField(default=0)
    drainage = models.CharField(default=0,max_length=20, choices=DRAINAGE_CHOICES)

    # FarmData
    land_tenure = models.CharField(max_length=50, choices=LAND_CHOICES ,null=True)
    total_size = models.IntegerField(default=0)
    arable_land_size = models.IntegerField(default=0)
    utilised_land_size = models.IntegerField(default=0)
    number_of_employees = models.IntegerField(default=0)
    farm_assets = models.CharField(max_length=20,null=True)

    def credit_score(self):
        weights = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Experience in farming
        if self.experience_in_farming > 5:
            ex_s = 0.9
        elif self.experience_in_farming < 3:
            ex_s = 0.5
        else:
            ex_s = 0.3

        # Household size
        if self.household_size > 5:
            h_s = 0.7
        else:
            h_s = 0.5

        # Accommodation status

        if self.accommodation_status == 'renting':
            a_s = 0.6
        else:
            a_s = 0.8

        # DEDICATION STATUS
        if self.dedication == 'Full time':
            d_s = 0.8
        else:
            d_s = 0.9

        # EDUCATION STATUS
        if self.education_level == 'Graduated':
            e_s = 0.9

        elif self.education_level == 'A level':
            e_s = 0.7

        elif self.education_level == 'O level':
            e_s = 0.5

        elif self.education_level == 'Primary level':
            e_s = 0.3

        else:
            e_s = 0

        # Total current debt
        if self.total_current_debt > 50:
            dt_s = 0.4
        else:
            dt_s = 0.6

        # Average monthly earnings
        if self.average_monthly_earnings >= 200:
            av_s = 0.6
        elif self.average_monthly_earnings < 50:
            av_s = 0.2
        else:
            av_s = 0.3

        # Annual/ Season turnover
        if self.annual_or_season_turnover >= 800:
            st_s = 0.7
        elif sturn < 300:
            st_s = 0.3
        else:
            st_s = 0.5

        # Most recent annual/ season profit
        if self.most_recent_annual_or_season_profit >= 300:
            sp_s = 0.7
        elif self.most_recent_annual_or_season_profit < 100:
            sp_s = 0.3
        else:
            sp_s = 0.5

        # Alternative source of income
        if self.alternative_source_of_income == 'salary':
            alt_s = 0.9
        else:
            alt_s = 0.5

        # Average temperature	25
        if self.average_temperature >= 25:
            av_s = 0.7
        else:
            av_s = 0.5

        # Moisture levels	45%
        if self.moisture_levels >= 50:
            mo_s = 0.8
        else:
            mo_s = 0.4

        # Altitude	1150
        if self.altitude >= 1150:
            al_s = 0.8
        else:
            al_s = 0.5

        # Drought frequences in past 10 years	1
        if self.drought_frequencies_in_past_10_years >= 3:
            dr_s = 0.3
        else:
            dr_s = 0.8

        # Floods frequencies in past 10 years	0
        if self.floods_frequencies_in_past_10_years >= 1:
            fl_s = 0.3
        else:
            fl_s = 0.9

        # Pest and Diseases frequency	mild
        if self.pest_and_diseases_frequency == 'Mild':
            pd_s = 0.8
        else:
            pd_s = 0.3

        # Soil type	Clay	0.7
        if self.soil_type == 'Clay':
            st_s = 0.7
        else:
            st_s = 0.5

        # Water content		0.8
        if self.water_content >= 50:
            wc_s = 0.8
        else:
            wc_s = 0.5

        # Temperature	20	0.6
        if self.temperature >= 20:
            tp_s = 0.6
        else:
            tp_s = 0.3
        # Potassium levels		0.2
        if self.potassium_levels >= 20:
            pt_s = 0.6
        else:
            pt_s = 0.2

        # Nitrogen Levels		0.3
        if self.nitrogen_Levels >= 20:
            nt_s = 0.6
        else:
            nt_s = 0.3

        # Drainage		0.2
        if self.drainage == 'Medium':
            dg_s = 0.2
        elif self.drainage == 'low':
            dg_s = 0.7
        else:
            dg_s = 0.1

        if self.land_tenure == 'Owner':
            lt_s = 0.9
        else:
            lt_s = 0.8

        # Total size	10ha	0.6	2
        if self.total_size > 10:
            ts_s = 0.8
        else:
            ts_s = 0.6
        # Arrable land size	8ha	0.7	4
        if self.arable_land_size >= 8:
            arr_s = 0.7
        else:
            arr_s = 0.5

        # Utilised land size	5ha	0.8	5
        if self.utilised_land_size >= 5:
            ut_s = 0.8
        else:
            ut_s = 0.4
        # Number of employees	3	0.5	1
        if numofe <= 3:
            ne_s = 0.5
        else:
            ne_s = 0.8
            # Farm assets	Irrigation equipment, 2 tractors, 1 plower, 1 disk harrow	1	1
        if self.farm_assets in ['irrigation equipment', 'tractors', 'plower', 'disk harrow']:
            fm_s = 1
        else:
            fm_s = 1

        landtw_score = 2 * lt_s
        totalzw_score = 2 * ts_s
        arrablezw_score = 4 * arr_s
        utilisedw_score = 5 * ut_s
        numofew_score = 1 * ne_s
        farmassw_score = 1 * fm_s

        all_fd = [landtw_score, totalzw_score, arrablezw_score, utilisedw_score, numofew_score, farmassw_score]

        edw_score = weights[2] * e_s
        dedw_score = weights[3] * d_s
        accw_score = weights[2] * a_s
        hsw_score = weights[2] * h_s
        expw_score = weights[6] * ex_s

        all_scores = [edw_score, dedw_score, accw_score, hsw_score, expw_score]

        debtw_score = 3 * dt_s
        avew_score = 4 * av_s
        sturnw_score = 7 * st_s
        sproftw_score = 2 * sp_s
        altsocw_score = 3 * alt_s

        all_f_scores = [debtw_score, avew_score, sturnw_score, sproftw_score, altsocw_score]

        # Weighted scores
        avtw_score = 7 * av_s
        moistlw_score = 5 * mo_s
        altitudew_score = 3 * al_s
        drougthfw_score = 6 * dr_s
        floodfw_score = 4 * fl_s
        pestdw_score = 5 * pd_s

        all_ = [avtw_score, moistlw_score, altitudew_score, drougthfw_score, floodfw_score, pestdw_score]

        # Weighted score
        soiltw_score = 4 * st_s
        watercw_score = 5 * wc_s
        tempw_score = 4 * tp_s
        potassw_score = 2 * pt_s
        nitrow_score = 2 * nt_s
        drainagew_score = 3 * dg_s

        all_soildw = [soiltw_score, watercw_score, tempw_score, potassw_score, nitrow_score, drainagew_score]
        sc_score = sum(all_soildw)
        farmc_score = sum(all_fd)
        wc_score = sum(all_)
        fc_score = sum(all_f_scores)
        pd_score = sum(all_scores)

        scores = [sc_score, farmc_score, wc_score, fc_score, farmc_score, pd_score]
        total_score = sum(scores)
        return total_score

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)


class Loan(models.Model):
    CATEGORY = (
        ('Farming', 'Farming'),
        ('Civil Servants', 'Civil Servants'),
        ('General', 'General'),

    )
    name_of_loan = models.CharField(max_length=200, null=True)
    amount = models.FloatField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name_of_loan


class Order(models.Model):
    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.loan.name_of_loan
