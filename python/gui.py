# gui.py - Refactored OOP version
import customtkinter as ctk
from calculator import BallisticsToTarget, OutOfRangeException

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class BallisticCalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title('Мираж-Гео : Ballistic Calculator')
        self.geometry("1600x768")
        
        # Initialize StringVars
        self.xCannon = ctk.StringVar()
        self.yCannon = ctk.StringVar()
        self.zCannon = ctk.StringVar()
        self.xTarget = ctk.StringVar()
        self.yTarget = ctk.StringVar()
        self.zTarget = ctk.StringVar()
        self.lenghtEntry = ctk.StringVar()
        self.powerEntry = ctk.StringVar()
        self.directionEntry = ctk.StringVar()
        
        self.varYaw = ctk.StringVar(value="---")
        self.varPitch = ctk.StringVar(value="---")
        self.varAirtime = ctk.StringVar(value="---")
        self.varAirtimeSeconds = ctk.StringVar(value="---")
        self.varFuzeTime = ctk.StringVar(value="---")
        self.varPrecision = ctk.StringVar(value="---")
        
        self.varYaw2 = ctk.StringVar(value="---")
        self.varPitch2 = ctk.StringVar(value="---")
        self.varAirtime2 = ctk.StringVar(value="---")
        self.varAirtimeSeconds2 = ctk.StringVar(value="---")
        self.varFuzeTime2 = ctk.StringVar(value="---")
        self.varPrecision2 = ctk.StringVar(value="---")
        
        self.statusMessage = ctk.StringVar(value="")
        
        self.setup_ui()
        self.bind("<Key>", self.control_button)
    
    def represents_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    
    def validate_integer_entry(self, P):
        return self.represents_int(P) or P == "" or P == "-"
    
    def control_button(self, *args):
        all_filled = all([
            self.xCannon.get(), self.yCannon.get(), self.zCannon.get(),
            self.xTarget.get(), self.yTarget.get(), self.zTarget.get(),
            self.lenghtEntry.get(), self.powerEntry.get(),
            self.directionEntry.get().strip()
        ])
        self.calculate_button.configure(state="normal" if all_filled else "disabled")
    
    def setup_ui(self):
        # Title
        title_label = ctk.CTkLabel(
            master=self, text="Мираж-Гео: Ballistic Calculator",
            font=("Roboto", 54), fg_color="#1E538D", corner_radius=20
        )
        title_label.pack(pady=20, padx=120, fill="both", expand=True)
        
        main_frame = ctk.CTkFrame(master=self, corner_radius=20)
        main_frame.pack(pady=30, padx=60, ipadx=40, fill="both", expand=True)
        main_frame.columnconfigure(0, weight=1)
        
        # Cannon / Target inputs
        cannon_frame = ctk.CTkFrame(master=main_frame, width=200)
        target_frame = ctk.CTkFrame(master=main_frame, width=200)
        cannon_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        target_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")
        
        vcmd = (self.register(self.validate_integer_entry), '%P')
        
        self._build_coordinate_inputs(cannon_frame, "Cannon Position",
                                       [("X:", self.xCannon), ("Y:", self.yCannon), ("Z:", self.zCannon)],
                                       vcmd)
        self._build_coordinate_inputs(target_frame, "Target Position",
                                       [("X:", self.xTarget), ("Y:", self.yTarget), ("Z:", self.zTarget)],
                                       vcmd)
        
        # Configuration
        config_frame = ctk.CTkFrame(master=main_frame)
        config_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky="ew")
        ctk.CTkLabel(config_frame, text="Cannon Configuration", font=("Roboto", 24)).pack(pady=10)
        
        for label, var in [("Cannon Length:", self.lenghtEntry),
                           ("Number of Powder Charges:", self.powerEntry),
                           ("Direction (east/west/north/south):", self.directionEntry)]:
            frame = ctk.CTkFrame(config_frame, fg_color="transparent")
            frame.pack(pady=5, fill="x", padx=20)
            ctk.CTkLabel(frame, text=label).pack(side="left", padx=5)
            entry = ctk.CTkEntry(frame, textvariable=var)
            entry.pack(side="left", fill="x", expand=True)
        
        # Button + Status
        self.calculate_button = ctk.CTkButton(
            master=main_frame, text="Calculate",
            command=self.calculate_angles, state="disabled", font=("Roboto", 20)
        )
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=20)
        
        self.status_label = ctk.CTkLabel(
            master=main_frame, textvariable=self.statusMessage,
            text_color="red", font=("Roboto", 16)
        )
        self.status_label.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Results
        results_frame = ctk.CTkFrame(master=main_frame)
        results_frame.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")
        ctk.CTkLabel(results_frame, text="Results", font=("Roboto", 24)).pack(pady=10)
        
        self._build_trajectory_results(results_frame, "Trajectory 1 (Direct)",
                                        [("Yaw:", self.varYaw), ("Pitch:", self.varPitch),
                                         ("Airtime (s):", self.varAirtimeSeconds),
                                         ("Fuze:", self.varFuzeTime), ("Precision:", self.varPrecision)])
        self._build_trajectory_results(results_frame, "Trajectory 2 (Arced)",
                                        [("Yaw:", self.varYaw2), ("Pitch:", self.varPitch2),
                                         ("Airtime (s):", self.varAirtimeSeconds2),
                                         ("Fuze:", self.varFuzeTime2), ("Precision:", self.varPrecision2)])
    
    def _build_coordinate_inputs(self, parent, title, entries, vcmd):
        ctk.CTkLabel(parent, text=title, font=("Roboto", 24)).pack(pady=10)
        for label, var in entries:
            frame = ctk.CTkFrame(parent, fg_color="transparent")
            frame.pack(pady=5, fill="x")
            ctk.CTkLabel(frame, text=label).pack(side="left", padx=5)
            entry = ctk.CTkEntry(frame, textvariable=var, validate="key", validatecommand=vcmd)
            entry.pack(side="left", fill="x", expand=True)
    
    def _build_trajectory_results(self, parent, title, fields):
        trajectory_frame = ctk.CTkFrame(parent)
        trajectory_frame.pack(pady=10, fill="x", padx=20)
        ctk.CTkLabel(trajectory_frame, text=title, font=("Roboto", 18)).pack(pady=5)
        
        results_row = ctk.CTkFrame(trajectory_frame, fg_color="transparent")
        results_row.pack(fill="x", padx=20)
        
        for i, (label, var) in enumerate(fields):
            ctk.CTkLabel(results_row, text=label).pack(side="left", padx=(0 if i == 0 else 15, 5))
            ctk.CTkLabel(results_row, textvariable=var, font=("Roboto", 14, "bold")).pack(side="left")
    
    def calculate_angles(self):
        try:
            cannon = (int(self.xCannon.get()), int(self.yCannon.get()), int(self.zCannon.get()))
            target = (int(self.xTarget.get()), int(self.yTarget.get()), int(self.zTarget.get()))
            power = int(self.powerEntry.get())
            direction = self.directionEntry.get().strip().lower()
            length = int(self.lenghtEntry.get())
            
            (yaw1, pitch1, airtime1, airtime_s1, fuze1, precision1), \
            (yaw2, pitch2, airtime2, airtime_s2, fuze2, precision2) = \
                BallisticsToTarget(cannon, target, power, direction, length)
            
            self.varYaw.set(f"{yaw1:.2f}")
            self.varPitch.set(f"{pitch1}")
            self.varAirtimeSeconds.set(f"{airtime_s1}")
            self.varFuzeTime.set(str(fuze1))
            self.varPrecision.set(f"{precision1}%")
            
            self.varYaw2.set(f"{yaw2:.2f}")
            self.varPitch2.set(f"{pitch2}")
            self.varAirtimeSeconds2.set(f"{airtime_s2}")
            self.varFuzeTime2.set(str(fuze2))
            self.varPrecision2.set(f"{precision2}%")
            
            self.statusMessage.set("✓ Calculation successful")
            self.status_label.configure(text_color="green")
            
        except ValueError:
            self.statusMessage.set("Error: All inputs must be valid integers!")
            self.status_label.configure(text_color="red")
        except OutOfRangeException as e:
            self.statusMessage.set(str(e))
            self.status_label.configure(text_color="red")
        except Exception as e:
            self.statusMessage.set(f"Unexpected error: {str(e)}")
            self.status_label.configure(text_color="red")


def main():
    app = BallisticCalculatorApp()
    app.mainloop()


if __name__ == "__main__":
    main()